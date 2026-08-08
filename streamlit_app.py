from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from ai_ux_workflow.contracts import PHASES
from ai_ux_workflow.gemini import generate_with_gemini
from ai_ux_workflow.pipeline import PipelineSession, artifact_zip, record_gate, repository_generator, run_phase
from ai_ux_workflow.security import valid_live_password


PAGES_URL = "https://karthiksoorya.github.io/ai-ux-design-pipeline/"

st.set_page_config(page_title="AI UX Design Pipeline", page_icon="✦", layout="wide")
st.markdown("""
<style>
.stApp {background: linear-gradient(145deg,#f7fbff 0%,#eef6ff 48%,#f8fffd 100%)}
.hero {padding:1.7rem 2rem;border-radius:22px;background:linear-gradient(120deg,#062d63,#075a8c 58%,#008f88);color:white;box-shadow:0 14px 35px #0c3d6a26}
.hero h1 {margin:0;font-size:2.35rem}.hero p{font-size:1.05rem;opacity:.9;margin-bottom:0}
.phase-card {position:relative;border:1px solid #bdd5ec;background:#ffffffde;border-radius:16px;padding:1rem;min-height:174px;box-shadow:0 5px 14px #164f7a0d;transition:.25s ease}
.phase-card::after {content:"";position:absolute;top:31px;right:-22px;width:22px;height:2px;background:#a9c8e5}
.phase-card.last::after {display:none}
.phase-card.active {border:2px solid #008f88;background:linear-gradient(145deg,#fff,#edfffb);box-shadow:0 10px 28px #008f8830;transform:translateY(-4px)}
.phase-card.approved {border-color:#48a97c;background:#f2fff8}
.phase-card.blocked {border-color:#d66a6a;background:#fff5f5}
.status {display:inline-flex;align-items:center;gap:.4rem;border-radius:999px;padding:.25rem .55rem;font-size:.68rem;font-weight:800;letter-spacing:.06em;color:#087b75;background:#ddf8f1}
.status::before {content:"";width:7px;height:7px;border-radius:50%;background:#008f88}
.active .status::before {animation:pulse 1.4s infinite;box-shadow:0 0 0 0 #008f8870}
.agent-chip {display:inline-block;margin:.2rem .15rem .1rem 0;padding:.22rem .48rem;border-radius:8px;background:#eaf3fc;color:#174a72;font-size:.76rem;font-weight:650}
.gate-line {margin-top:.65rem;padding-top:.55rem;border-top:1px dashed #b9cee1;font-size:.76rem;color:#486781}
.pipeline-strip {display:grid;grid-template-columns:repeat(4,1fr);gap:.6rem;margin:.9rem 0 1.2rem}.pipeline-node {position:relative;padding:.65rem .75rem;border:1px solid #bfd5e9;border-radius:12px;background:#ffffffcc;color:#31526e;font-size:.76rem}.pipeline-node strong {display:block;color:#123c61;font-size:.86rem}.pipeline-node.current {border:2px solid #008f88;background:#edfffb;box-shadow:0 6px 18px #008f8826}.pipeline-node.done {border-color:#58ad80;background:#f1fff7}.pipeline-node::after {content:"→";position:absolute;right:-.55rem;top:35%;z-index:2;color:#6c91af;font-weight:800}.pipeline-node:last-child::after {display:none}
.side-phase {margin:.55rem 0;padding:.7rem;border:1px solid #547ca4;border-radius:12px;background:#ffffff12}.side-phase.current {border-color:#45d6c5;background:#008f8830;box-shadow:inset 3px 0 #45d6c5}.side-phase.done {border-color:#6ac497;background:#39a67825}.side-phase strong,.side-phase small {display:block;color:#f7fbff !important}.side-phase small {margin-top:.25rem;color:#b9d8ee !important}
.pipeline-console {padding:1rem 1.2rem;border-radius:16px;background:#082f5b;color:#edf8ff;box-shadow:inset 4px 0 #16b8a6,0 8px 22px #082f5b25}
.pipeline-console small {color:#9fd8ed}.pipeline-console strong {color:#fff}
.run-overlay {position:fixed;z-index:9999;top:3.6rem;left:50%;transform:translateX(-50%);width:min(780px,calc(100vw - 2rem));padding:.75rem 1rem;border:1px solid #45d6c5;border-radius:14px;background:#062d63f2;color:#fff;box-shadow:0 12px 34px #061f3d55;backdrop-filter:blur(10px);pointer-events:none}
.run-overlay-head {display:flex;justify-content:space-between;gap:1rem;font-size:.82rem;font-weight:750}.run-overlay-detail {margin-top:.25rem;color:#bcecf0;font-size:.74rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.run-overlay-track {height:7px;margin-top:.55rem;border-radius:999px;background:#ffffff25;overflow:hidden}.run-overlay-fill {height:100%;border-radius:999px;background:linear-gradient(90deg,#11b9aa,#62e7cf);transition:width .2s ease;box-shadow:0 0 12px #35e0c8}
@keyframes pulse {0%{box-shadow:0 0 0 0 #008f8870}70%{box-shadow:0 0 0 9px #008f8800}100%{box-shadow:0 0 0 0 #008f8800}}
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
[data-testid="stSidebar"] [data-testid="stButton"] button,
[data-testid="stSidebar"] [data-testid="stButton"] button p,
[data-testid="stSidebar"] [data-testid="stLinkButton"] a,
[data-testid="stSidebar"] [data-testid="stLinkButton"] a p {color:#0b3158 !important;font-weight:700 !important}
[data-testid="stSidebar"] input {color:#102a43 !important;background:#f7fbff !important}
[data-testid="stSidebar"] input:disabled {-webkit-text-fill-color:#34516f !important;opacity:1 !important}
[data-testid="stSidebar"] hr {border-color:#6f91b5 !important}
[data-testid="stSidebarCollapseButton"] button,
[data-testid="stSidebarCollapsedControl"] button {background:#0b4b7f !important;border:1px solid #69d7cd !important;border-radius:9px !important;box-shadow:0 3px 10px #001c3840 !important}
[data-testid="stSidebarCollapseButton"] button:hover,
[data-testid="stSidebarCollapsedControl"] button:hover {background:#087b75 !important;border-color:#b9fff6 !important}
[data-testid="stSidebarCollapseButton"] button span,
[data-testid="stSidebarCollapsedControl"] button span,
[data-testid="stSidebarCollapseButton"] button svg,
[data-testid="stSidebarCollapsedControl"] button svg {color:#ffffff !important;fill:#ffffff !important;opacity:1 !important}
[data-testid="stSidebarCollapseButton"] button:focus-visible,
[data-testid="stSidebarCollapsedControl"] button:focus-visible {outline:3px solid #f7d154 !important;outline-offset:2px !important}
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


@st.dialog("Confirm human gate decision")
def confirm_gate_decision(phase_number: int, decision: str) -> None:
    selected_phase = PHASES[phase_number - 1]
    st.markdown(f"### Gate {selected_phase.gate_id}: {decision}")
    consequences = {
        "APPROVE": f"Advance to Phase {min(phase_number + 1, 4)} after recording your explicit approval.",
        "REVISE": "Keep this phase active and rerun only affected current/downstream work.",
        "REJECT": "Block further execution for this session until it is reset.",
    }
    st.info(consequences[decision])
    st.caption("This is a human decision. No agent can record it on your behalf.")
    confirm, cancel = st.columns(2)
    if confirm.button(f"Confirm {decision}", type="primary" if decision == "APPROVE" else "secondary", use_container_width=True):
        record_gate(state, phase_number, decision)
        st.rerun()
    if cancel.button("Cancel", use_container_width=True):
        st.rerun()

with st.sidebar:
    st.header("Pipeline console")
    st.caption("Use the arrow above to collapse this panel and expand the workspace.")
    controls_tab, phases_tab = st.tabs(["Controls", "Phases"])
    with controls_tab:
        mode = st.radio("Execution mode", ["Demo", "Live AI"], help="Demo uses checked-in synthetic artifacts. Live AI calls Gemini.")
        model = st.text_input("Gemini model", value=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"), disabled=mode == "Demo")
        live_password = ""
        if mode == "Live AI":
            live_password = st.text_input(
                "Live AI access password",
                type="password",
                help="This shared password is checked server-side and is separate from the Gemini API key.",
            )
        synthetic_ok = st.checkbox("Inputs are synthetic demo data", value=mode == "Demo")
        if st.button("Reset session", use_container_width=True):
            st.session_state.pipeline = PipelineSession()
            st.session_state.uploaded_inputs = {}
            st.session_state.final_dialog_shown = False
            st.rerun()
        st.divider()
        st.link_button("Open public documentation", PAGES_URL, use_container_width=True)
        st.caption("Agents never approve gates. Every approval shown here is a human action.")
    with phases_tab:
        for sidebar_phase in PHASES:
            sidebar_status = state.phase_status[sidebar_phase.number]
            sidebar_class = "current" if sidebar_phase.number == state.current_phase and sidebar_status != "APPROVED" else "done" if sidebar_status == "APPROVED" else ""
            sidebar_agents = " + ".join(Path(agent).stem.replace("-", " ").title() for agent in sidebar_phase.agents)
            st.markdown(f'<div class="side-phase {sidebar_class}"><strong>{sidebar_phase.number}. {sidebar_phase.name}</strong><small>{sidebar_agents}</small><small>{sidebar_status} · {sidebar_phase.gate_id}: {state.gate_status[sidebar_phase.number]}</small></div>', unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>AI UX Discovery-to-Prototype Pipeline</h1><p>BRD → Research → Ideation → Design → Validation → Verified Workable Prototype</p></div>', unsafe_allow_html=True)
execution_hud = st.empty()
st.write("")

strip_nodes = []
for strip_phase in PHASES:
    strip_status = state.phase_status[strip_phase.number]
    strip_class = "current" if strip_phase.number == state.current_phase and strip_status != "APPROVED" else "done" if strip_status == "APPROVED" else ""
    strip_nodes.append(f'<div class="pipeline-node {strip_class}"><strong>{strip_phase.number}. {strip_phase.name}</strong>{strip_status} · {strip_phase.gate_id}</div>')
st.markdown(f'<div class="pipeline-strip">{"".join(strip_nodes)}</div>', unsafe_allow_html=True)

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
active_agents = " + ".join(Path(agent).stem.replace("-", " ").title() for agent in phase.agents)
mode_note = "Synthetic artifact replay — no model tokens used" if mode == "Demo" else "Live Gemini execution — protected by password"
st.markdown(f'<div class="pipeline-console"><small>CURRENT PIPELINE ACTIVITY</small><br><strong>{active_agents}</strong><br><small>{mode_note} · waiting to execute {len(phase.skills)} declared skills</small></div>', unsafe_allow_html=True)
st.write("")
c1, c2 = st.columns([1, 2])
with c1:
    can_run = state.phase_status[phase.number] in ("NOT STARTED", "REVISION REQUIRED")
    if st.button(f"Run Phase {phase.number}", type="primary", disabled=not can_run, use_container_width=True):
        try:
            if mode == "Demo":
                generator = repository_generator(ROOT)
            else:
                configured_password = os.getenv("LIVE_AI_PASSWORD", "") or st.secrets.get("LIVE_AI_PASSWORD", "")
                if not configured_password:
                    raise ValueError("Live AI is locked because LIVE_AI_PASSWORD is not configured by the app owner.")
                if not valid_live_password(live_password, configured_password):
                    raise ValueError("Incorrect Live AI access password.")
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
            with st.status(f"Dispatching Phase {phase.number} agents…", expanded=True) as execution_status:
                st.write(f"**Agents:** {active_agents}")
                progress = st.progress(0, text="Preparing authoritative workflow context")
                execution_hud.markdown(f'<div class="run-overlay"><div class="run-overlay-head"><span>Phase {phase.number} · {active_agents}</span><span>0%</span></div><div class="run-overlay-detail">Preparing authoritative workflow context</div><div class="run-overlay-track"><div class="run-overlay-fill" style="width:0%"></div></div></div>', unsafe_allow_html=True)
                for index, skill in enumerate(phase.skills, 1):
                    percent = round(index / (len(phase.skills) + 1) * 100)
                    progress.progress(percent / 100, text=f"Applying {skill}")
                    execution_hud.markdown(f'<div class="run-overlay"><div class="run-overlay-head"><span>Phase {phase.number} · {active_agents}</span><span>{percent}%</span></div><div class="run-overlay-detail">Applying {skill}</div><div class="run-overlay-track"><div class="run-overlay-fill" style="width:{percent}%"></div></div></div>', unsafe_allow_html=True)
                    st.write(f"`{index:02d}`  {skill}")
                    if mode == "Demo":
                        time.sleep(0.22)
                run_phase(state, phase.number, generator)
                progress.progress(1.0, text=f"Validating declared outputs for Gate {phase.gate_id}")
                execution_hud.markdown(f'<div class="run-overlay"><div class="run-overlay-head"><span>Phase {phase.number} · Output validation</span><span>100%</span></div><div class="run-overlay-detail">Preparing Gate {phase.gate_id} for explicit human review</div><div class="run-overlay-track"><div class="run-overlay-fill" style="width:100%"></div></div></div>', unsafe_allow_html=True)
                execution_status.update(label=f"Phase {phase.number} complete — Gate {phase.gate_id} review required", state="complete", expanded=True)
                time.sleep(0.35)
                execution_hud.empty()
            st.success(f"Phase {phase.number} is ready for Gate {phase.gate_id}.")
            st.rerun()
        except Exception as exc:
            execution_hud.empty()
            st.error(str(exc))
with c2:
    st.markdown("**Declared skill sequence**")
    st.write(" → ".join(phase.skills))

phase_artifacts = [(path, state.artifacts[path]) for path in phase.outputs if path in state.artifacts]
if phase_artifacts:
    st.subheader(f"3. Gate {phase.gate_id} — Human review")
    if state.phase_status[phase.number] == "READY FOR REVIEW":
        st.warning("Review the artifacts below, then record an explicit human decision.")
        a, r, x = st.columns(3)
        for column, decision, label in ((a, "APPROVE", "✓ APPROVE"), (r, "REVISE", "↺ REVISE"), (x, "REJECT", "✕ REJECT")):
            if column.button(label, use_container_width=True, type="primary" if decision == "APPROVE" else "secondary"):
                confirm_gate_decision(phase.number, decision)
    tabs = st.tabs([Path(path).name for path, _ in phase_artifacts])
    for tab, (path, content) in zip(tabs, phase_artifacts):
        with tab:
            st.caption(path)
            st.markdown(content)

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
