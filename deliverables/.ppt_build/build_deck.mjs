import fs from "node:fs/promises";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const ROOT = "C:/Users/Karthik/OneDrive/Documents/AI UX/ai-ux-design-pipeline";
const OUT = `${ROOT}/deliverables`;
const SHOTS = `${OUT}/screenshots`;
const W = 1280, H = 720;
const C = { navy: "#0B356A", navy2: "#123E73", teal: "#079A92", aqua: "#27C5BB", ink: "#102A43", muted: "#5F7287", pale: "#EEF6FD", white: "#FFFFFF", line: "#C7D9EA", green: "#16865C", amber: "#E5A400" };

async function bytes(path) {
  const b = await fs.readFile(path);
  return b.buffer.slice(b.byteOffset, b.byteOffset + b.byteLength);
}
function box(slide, x, y, w, h, fill, radius="rounded-xl", line="none") {
  return slide.shapes.add({ geometry:"roundRect", position:{left:x,top:y,width:w,height:h}, fill, line:{style:"solid",fill:line,width:line==="none"?0:1}, borderRadius:radius });
}
function txt(slide, text, x, y, w, h, size=20, color=C.ink, bold=false, align="left") {
  const s=slide.shapes.add({geometry:"textbox",position:{left:x,top:y,width:w,height:h},fill:"none",line:{style:"solid",fill:"none",width:0}});
  s.text=text; s.text.style={fontSize:size,color,bold,alignment:align,fontFamily:"Aptos"}; return s;
}
function rule(slide,x,y,w,color=C.aqua,h=5){slide.shapes.add({geometry:"rect",position:{left:x,top:y,width:w,height:h},fill:color,line:{style:"solid",fill:"none",width:0}})}
async function img(slide,path,x,y,w,h,fit="cover",radius="rounded-xl") {
  slide.images.add({blob:await bytes(path),contentType:"image/png",alt:"Project screenshot",fit,position:{left:x,top:y,width:w,height:h},geometry:"roundRect",borderRadius:radius});
}
function title(slide, eyebrow, heading, sub="") {
  txt(slide,eyebrow.toUpperCase(),64,44,1120,24,15,C.teal,true);
  txt(slide,heading,64,75,1120,58,37,C.ink,true);
  if(sub) txt(slide,sub,64,136,1120,38,18,C.muted,false);
  rule(slide,64,178,92,C.aqua,5);
}
function footer(slide,n){txt(slide,`AI UX DESIGN PIPELINE  •  ${String(n).padStart(2,"0")}`,64,682,500,18,12,"#7790A8",true);}
function addNotes(slide, lines){ slide.addNotes?.(`[Sources]\n${lines.join("\n")}\n[/Sources]`); }

const p=Presentation.create({slideSize:{width:W,height:H}});

// 1 — Title
{
  const s=p.slides.add(); s.background.fill=C.pale;
  box(s,0,0,W,720,C.navy,"rounded-none");
  s.shapes.add({geometry:"rect",position:{left:890,top:0,width:390,height:720},fill:C.teal,line:{style:"solid",fill:"none",width:0}});
  txt(s,"AI UX",70,78,430,28,18,C.aqua,true);
  txt(s,"Discovery-to-Prototype\nPipeline",70,132,760,164,58,C.white,true);
  txt(s,"A governed multi-agent process that turns a BRD into a human-verified workable prototype.",70,326,690,84,24,"#D7E9F8",false);
  rule(s,70,445,210,C.aqua,7);
  txt(s,"RUNNABLE PUBLIC DEMO",70,476,330,28,16,C.aqua,true);
  txt(s,"ai-ux-design-pipeline.streamlit.app",70,514,600,32,21,C.white,true);
  txt(s,"4",955,150,160,120,92,C.white,true,"center");
  txt(s,"specialized phase agents",930,268,210,62,22,C.white,true,"center");
  txt(s,"D1–D4",955,412,160,65,48,"#D7FFF8",true,"center");
  txt(s,"explicit human gates",930,480,210,62,22,C.white,true,"center");
  addNotes(s,["https://ai-ux-design-pipeline.streamlit.app/"]);
}

// 2 — Differentiator
{
  const s=p.slides.add(); s.background.fill=C.white;
  title(s,"The differentiator","Specialized agents own the work; the orchestrator only routes it","Each agent invokes reusable skills and hands traceable artifacts to the next governed stage.");
  await img(s,`${OUT}/AI_UX_Specialized_Agent_Flow_Infographic.png`,50,200,1180,452,"contain","rounded-lg");
  footer(s,2);
}

// 3 — Public runner
{
  const s=p.slides.add(); s.background.fill=C.pale;
  title(s,"Runnable experience","The public runner makes the architecture visible","Demo mode uses predefined synthetic inputs; Live AI can be protected and configured separately.");
  await img(s,`${SHOTS}/01-demo-landing.png`,54,208,820,446,"contain");
  box(s,910,220,306,112,C.navy); txt(s,"01",932,238,54,38,28,C.aqua,true); txt(s,"Mode is always visible",993,238,198,46,20,C.white,true); txt(s,"DEMO avoids token use; LIVE exposes secured runner controls.",932,284,252,40,15,"#D5E7F8");
  box(s,910,350,306,112,C.white,"rounded-xl",C.line); txt(s,"02",932,368,54,38,28,C.teal,true); txt(s,"Phases stay in view",993,368,198,46,20,C.ink,true); txt(s,"The vertical rail shows agent ownership and gate state.",932,414,252,40,15,C.muted);
  box(s,910,480,306,112,C.white,"rounded-xl",C.line); txt(s,"03",932,498,54,38,28,C.teal,true); txt(s,"Skills are explicit",993,498,198,46,20,C.ink,true); txt(s,"The declared sequence is visible before execution begins.",932,544,252,40,15,C.muted);
  footer(s,3); addNotes(s,["https://ai-ux-design-pipeline.streamlit.app/"]);
}

// 4 — Execution
{
  const s=p.slides.add(); s.background.fill=C.white;
  title(s,"Execution feels real","Progress exposes the active agent and skill","The runner shows movement without pretending synthetic demo outputs are real research.");
  await img(s,`${SHOTS}/02-phase-1-running.png`,54,208,900,440,"contain");
  txt(s,"57%",997,232,190,60,50,C.navy,true,"center");
  txt(s,"active progress",997,292,190,28,18,C.teal,true,"center");
  rule(s,1018,345,150,C.aqua,6);
  txt(s,"UX Research Agent",982,380,220,32,21,C.ink,true,"center");
  txt(s,"+",1055,414,74,30,24,C.teal,true,"center");
  txt(s,"Requirements Challenge Agent",978,450,230,58,20,C.ink,true,"center");
  txt(s,"Current skill:\ndebate-synthesis-skill",985,536,214,60,17,C.muted,false,"center");
  footer(s,4);
}

// 5 — Governance
{
  const s=p.slides.add(); s.background.fill=C.pale;
  title(s,"Human governance","No agent can approve its own work","D1–D4 require an explicit reviewer decision before the next phase becomes eligible.");
  await img(s,`${SHOTS}/04-d1-confirmation.png`,54,210,790,444,"contain");
  txt(s,"APPROVE",900,226,260,32,23,C.green,true); txt(s,"Record the decision and advance exactly one phase.",900,264,280,54,17,C.muted);
  rule(s,900,338,260,C.line,2);
  txt(s,"REVISE",900,362,260,32,23,C.amber,true); txt(s,"Rerun only the minimum affected downstream work.",900,400,280,54,17,C.muted);
  rule(s,900,474,260,C.line,2);
  txt(s,"REJECT",900,498,260,32,23,"#B53B3B",true); txt(s,"Block the workflow; no automatic progression.",900,536,280,54,17,C.muted);
  footer(s,5);
}

// 6 — Verified outcome
{
  const s=p.slides.add(); s.background.fill=C.white;
  title(s,"Governed outcome","The prototype is ‘verified’ only after D4 approval","The completion message retains the synthetic-validation and accessibility limitations.");
  await img(s,`${SHOTS}/05-verified-prototype.png`,54,208,835,445,"contain");
  box(s,925,224,260,210,C.navy);
  txt(s,"✓",1003,244,100,70,52,C.aqua,true,"center");
  txt(s,"4 phases",965,320,180,32,24,C.white,true,"center");
  txt(s,"4 human gates",965,360,180,32,24,C.white,true,"center");
  txt(s,"1 verified prototype",950,400,210,34,22,"#D7FFF8",true,"center");
  txt(s,"Verification is scoped—not a claim of real-participant evidence or formal WCAG certification.",932,476,246,100,17,C.muted,false,"center");
  footer(s,6);
}

// 7 — How to test
{
  const s=p.slides.add(); s.background.fill=C.pale;
  title(s,"Try it now","A two-minute demo shows the full governed journey","Start in Demo mode; switch to Live AI only with the configured password and API secret.");
  await img(s,`${SHOTS}/06-workable-prototype.png`,660,202,560,315,"contain");
  txt(s,"DEMO MODE",64,220,260,30,20,C.teal,true);
  txt(s,"1  Keep Live AI mode OFF\n2  Run each phase\n3  Review artifacts at D1–D4\n4  Explicitly APPROVE each gate\n5  Open the workable prototype",64,268,480,190,22,C.ink,false);
  txt(s,"LIVE AI MODE",64,500,260,30,20,C.navy,true);
  txt(s,"Switch Live AI ON → enter the access password → use configured Gemini credentials.",64,540,500,68,18,C.muted);
  box(s,660,548,560,72,C.navy); txt(s,"https://ai-ux-design-pipeline.streamlit.app/",684,568,510,32,20,C.white,true,"center");
  footer(s,7); addNotes(s,["https://ai-ux-design-pipeline.streamlit.app/","https://karthiksoorya.github.io/ai-ux-design-pipeline/prototype/","https://karthiksoorya.github.io/ai-ux-design-pipeline/"]);
}

await fs.mkdir(`${OUT}/.ppt_build/rendered`,{recursive:true});
for (const [i,s] of p.slides.items.entries()) {
  const png=await p.export({slide:s,format:"png",scale:1});
  await fs.writeFile(`${OUT}/.ppt_build/rendered/slide-${String(i+1).padStart(2,"0")}.png`,new Uint8Array(await png.arrayBuffer()));
  const layout=await s.export({format:"layout"});
  await fs.writeFile(`${OUT}/.ppt_build/rendered/slide-${String(i+1).padStart(2,"0")}.layout.json`,await layout.text());
}
const montage=await p.export({format:"webp",montage:true,scale:1});
await fs.writeFile(`${OUT}/AI_UX_Pipeline_Demonstration_Guide_Montage.webp`,new Uint8Array(await montage.arrayBuffer()));
const pptx=await PresentationFile.exportPptx(p);
await pptx.save(`${OUT}/AI_UX_Pipeline_Demonstration_Guide.pptx`);

