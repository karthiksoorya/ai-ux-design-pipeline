from __future__ import annotations

import os
import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from ai_ux_workflow.contracts import PHASES
from ai_ux_workflow.gemini import generate_with_gemini
from ai_ux_workflow.pipeline import PipelineSession, artifact_zip, record_gate, repository_generator, run_phase


PAGES_URL = "https://karthiksoorya.github.io/ai-ux-design-pipeline/"

st.set_page_config(page_title="AI UX Design Pipeline", page_icon="✦", layout="wide")
st.markdown("""
<style>
.stApp {background: linear-gradient(145deg,#f7fbff 0%,#eef6ff 48%,#f8fffd 100%)}
.hero {padding:1.7rem 2rem;border-radius:22px;background:linear-gradient(120deg,#062d63,#075a8c 58%,#008f88);color:white;box-shadow:0 14px 35px #0c3d6a26}
.hero h1 {margin:0;font-size:2.35rem}.hero p{font-size:1.05rem;opacity:.9;margin-bottom:0}
.phase-card {border:1px solid #bdd5ec;background:#ffffffcc;border-radius:14px;padding:.9rem;min-height:130px}
.status {font-size:.72rem;font-weight:800;letter-spacing:.06em;color:#087b75}
[data-testid="stSidebar"] {background:#062d63;color:white}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"],
[data-testid="stSidebar"] [role="radiogroup"] label span,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {color:#f7fbff !important}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {color:#f7fbff !important}
[data-testid="stSidebar"] input {color:#102a43 !important;background:#f7fbff !important}
[data-testid="stSidebar"] input:disabled {-webkit-text-fill-color:#34516f !important;opacity:1 !important}
[data-testid="stSidebar"] hr {border-color:#6f91b5 !important}
</style>
""", unsafe_allow_html=True)

if "pipeline" not in st.session_state:
    st.session_state.pipeline = PipelineSession()
if "uploaded_inputs" not in st.session_state:
    st.session_state.uploaded_inputs = {}
if "final_dialog_shown" not in st.session_state:
    st.session_state.final_dialog_shown = False
state: PipelineSession = st.session_state.pipeline


@st.dialog("✓ Verified Workable Prototype", width="large")
def show_final_result() -> None:
    st.success("All four phases and D1–D4 human gates are approved.")
    st.markdown("""
### The pipeline is complete

The prototype is verified **within the documented synthetic-demo and synthetic-validation limits**. This does not represent real-participant usability evidence or a formal accessibility-compliance certification.
""")
    left, right = st.columns(2)
    with left:
        st.link_button("Open workable prototype ↗", PAGES_URL + "prototype/", type="primary", use_container_width=True)
    with right:
        st.link_button("Open pipeline documentation ↗", PAGES_URL, use_container_width=True)
    st.download_button(
        "Download all workflow artifacts (.zip)",
        artifact_zip(state),
        "ai-ux-pipeline-artifacts.zip",
        "application/zip",
        use_container_width=True,
    )

with st.sidebar:
    st.header("Runner controls")
    mode = st.radio("Execution mode", ["Demo", "Live AI"], help="Demo uses checked-in synthetic artifacts. Live AI calls Gemini.")
    model = st.text_input("Gemini model", value=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"), disabled=mode == "Demo")
    synthetic_ok = st.checkbox("Inputs are synthetic demo data", value=mode == "Demo")
    if st.button("Reset session", use_container_width=True):
        st.session_state.pipeline = PipelineSession()
        st.session_state.uploaded_inputs = {}
        st.session_state.final_dialog_shown = False
        st.rerun()
    st.divider()
    st.link_button("Open public documentation", PAGES_URL, use_container_width=True)
    st.caption("Agents never approve gates. Every approval shown here is a human action.")

st.markdown('<div class="hero"><h1>AI UX Discovery-to-Prototype Pipeline</h1><p>BRD → Research → Ideation → Design → Validation → Verified Workable Prototype</p></div>', unsafe_allow_html=True)
st.write("")

cols = st.columns(4)
for phase, col in zip(PHASES, cols):
    with col:
        agents = "<br>".join(Path(agent).stem.replace("-", " ").title() for agent in phase.agents)
        st.markdown(f'<div class="phase-card"><div class="status">{state.phase_status[phase.number]}</div><h3>Phase {phase.number}: {phase.name}</h3><div>{agents}</div><small>Gate {phase.gate_id}: {state.gate_status[phase.number]}</small></div>', unsafe_allow_html=True)

st.subheader("1. Project inputs")
uploads = st.file_uploader("Upload Markdown or text inputs", type=["md", "txt"], accept_multiple_files=True)
for upload in uploads:
    st.session_state.uploaded_inputs[upload.name] = upload.getvalue().decode("utf-8", errors="replace")
input_names = list(st.session_state.uploaded_inputs)
if mode == "Demo" and not input_names:
    input_names = [path.name for path in sorted((ROOT / "projects/starter/input").glob("*")) if path.is_file()]
st.caption("Active inputs: " + (", ".join(input_names) if input_names else "None"))

phase = PHASES[state.current_phase - 1]
st.subheader(f"2. Execute Phase {phase.number} — {phase.name}")
c1, c2 = st.columns([1, 2])
with c1:
    can_run = state.phase_status[phase.number] in ("NOT STARTED", "REVISION REQUIRED")
    if st.button(f"Run Phase {phase.number}", type="primary", disabled=not can_run, use_container_width=True):
        try:
            if mode == "Demo":
                generator = repository_generator(ROOT)
            else:
                if not synthetic_ok:
                    raise ValueError("Confirm that live inputs are synthetic demo data before using the free-tier model.")
                api_key = os.getenv("GEMINI_API_KEY", "") or st.secrets.get("GEMINI_API_KEY", "")
                if not api_key:
                    raise ValueError("GEMINI_API_KEY is not configured in Streamlit secrets.")
                supplied = dict(st.session_state.uploaded_inputs)
                if not supplied and phase.number == 1:
                    raise ValueError("Upload at least one BRD or supporting source for Live AI mode.")
                supplied.update(state.artifacts)
                generator = lambda p, _: generate_with_gemini(ROOT, p, supplied, api_key, model)
            with st.spinner(f"{', '.join(Path(a).stem for a in phase.agents)} is working…"):
                run_phase(state, phase.number, generator)
            st.success(f"Phase {phase.number} is ready for Gate {phase.gate_id}.")
            st.rerun()
        except Exception as exc:
            st.error(str(exc))
with c2:
    st.markdown("**Declared skill sequence**")
    st.write(" → ".join(phase.skills))

phase_artifacts = [(path, state.artifacts[path]) for path in phase.outputs if path in state.artifacts]
if phase_artifacts:
    st.subheader(f"3. Gate {phase.gate_id} — Human review")
    tabs = st.tabs([Path(path).name for path, _ in phase_artifacts])
    for tab, (path, content) in zip(tabs, phase_artifacts):
        with tab:
            st.caption(path)
            st.markdown(content)
    if state.phase_status[phase.number] == "READY FOR REVIEW":
        st.warning("Review all artifacts. Only your explicit APPROVE can advance the workflow.")
        a, r, x = st.columns(3)
        for column, decision in ((a, "APPROVE"), (r, "REVISE"), (x, "REJECT")):
            if column.button(decision, use_container_width=True, type="primary" if decision == "APPROVE" else "secondary"):
                record_gate(state, phase.number, decision)
                st.rerun()

if state.artifacts:
    st.divider()
    st.download_button("Download generated artifacts (.zip)", artifact_zip(state), "ai-ux-pipeline-artifacts.zip", "application/zip")
    with st.expander("Execution log"):
        st.code("\n".join(state.logs))

if state.gate_status[4] == "APPROVE":
    st.markdown("""
<div style="margin-top:1rem;padding:1.4rem 1.6rem;border:2px solid #008f88;border-radius:18px;background:linear-gradient(120deg,#e8fff9,#eef6ff);box-shadow:0 10px 28px #087b7526">
  <div style="font-size:.78rem;font-weight:800;letter-spacing:.08em;color:#087b75">D4 APPROVED</div>
  <h2 style="margin:.25rem 0;color:#063a63">Verified Workable Prototype</h2>
  <p style="margin:0;color:#294861">The governed pipeline is complete within the documented synthetic-validation limits.</p>
</div>
""", unsafe_allow_html=True)
    if st.button("View final result", type="primary", use_container_width=True):
        st.session_state.final_dialog_shown = True
        show_final_result()
    elif not st.session_state.final_dialog_shown:
        st.session_state.final_dialog_shown = True
        show_final_result()
