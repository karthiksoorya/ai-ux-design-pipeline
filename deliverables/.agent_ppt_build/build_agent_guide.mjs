import fs from "node:fs/promises";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const ROOT="C:/Users/Karthik/OneDrive/Documents/AI UX/ai-ux-design-pipeline";
const OUT=`${ROOT}/deliverables`;
const TMP=`${OUT}/.agent_ppt_build`;
const W=1280,H=720;
const C={navy:"#0B356A",navy2:"#174A7E",teal:"#079A92",aqua:"#29C7BC",ink:"#102A43",muted:"#61758A",pale:"#EEF6FD",white:"#FFFFFF",line:"#C8DBEB",green:"#16865C",amber:"#E6A300",red:"#B63D42",lav:"#6C63B5"};

function shape(s,geo,x,y,w,h,fill,line="none",r="rounded-xl"){
  const config={geometry:geo,position:{left:x,top:y,width:w,height:h},fill,line:{style:"solid",fill:line,width:line==="none"?0:1}};
  if(["rect","textbox","roundRect"].includes(geo)) config.borderRadius=r;
  return s.shapes.add(config);
}
function text(s,t,x,y,w,h,size=20,color=C.ink,bold=false,align="left"){
  const z=shape(s,"textbox",x,y,w,h,"none"); z.text=t; z.text.style={fontFamily:"Aptos",fontSize:size,color,bold,alignment:align}; return z;
}
function rule(s,x,y,w,color=C.aqua,h=5){shape(s,"rect",x,y,w,h,color);}
function title(s,eyebrow,heading,sub=""){
  text(s,eyebrow.toUpperCase(),64,38,1120,22,14,C.teal,true);
  text(s,heading,64,66,1140,54,37,C.ink,true);
  if(sub) text(s,sub,64,126,1140,42,18,C.muted);
  rule(s,64,178,92);
}
function footer(s,n){text(s,`AI UX AGENT WORKFLOW GUIDE  •  ${String(n).padStart(2,"0")}`,64,682,550,18,12,"#7890A5",true);}
function icon(s,label,x,y,color=C.navy){shape(s,"ellipse",x,y,58,58,color);text(s,label,x,y+11,58,36,24,C.white,true,"center");}
function connector(s,x1,y1,x2,y2,color=C.line,w=3){
  s.shapes.add({geometry:"line",position:{left:x1,top:y1,width:x2-x1,height:y2-y1},fill:"none",line:{style:"solid",fill:color,width:w,endArrowType:"triangle"}});
}
function skillRow(s,num,name,desc,y,color=C.teal){
  shape(s,"ellipse",90,y,38,38,color); text(s,String(num),90,y+6,38,24,17,C.white,true,"center");
  text(s,name,146,y-2,315,28,19,C.ink,true); text(s,desc,146,y+27,500,42,16,C.muted);
}
function compactSkillRow(s,num,name,desc,y,color=C.green){
  shape(s,"ellipse",90,y,38,38,color); text(s,String(num),90,y+6,38,24,17,C.white,true,"center");
  text(s,name,146,y-1,315,25,18,C.ink,true); text(s,desc,146,y+24,500,24,15,C.muted);
}
function sidePanel(s,output,guardrail,value){
  shape(s,"roundRect",750,218,458,125,C.navy); text(s,`OUTPUT & HANDOFF\n${output}`,778,240,400,84,17,C.white,true);
  shape(s,"roundRect",750,362,458,116,C.white,C.line); text(s,`GUARDRAIL — ${guardrail}`,778,390,400,70,16,C.ink);
  shape(s,"roundRect",750,497,458,145,C.teal); text(s,`WHY IT MATTERS — ${value}`,778,530,400,88,17,C.white,true);
}

const p=Presentation.create({slideSize:{width:W,height:H}});

// 1 title
{
 const s=p.slides.add(); s.background.fill=C.navy;
 shape(s,"rect",880,0,400,H,C.teal);
 text(s,"AI UX",72,72,240,26,17,C.aqua,true);
 text(s,"Specialized Agent\nWorkflow Guide",72,130,700,155,56,C.white,true);
 text(s,"What each agent receives, which skills it invokes, what those skills do, and how evidence moves safely to the next phase.",72,326,680,98,24,"#D8E9F8");
 rule(s,72,462,210,C.aqua,7);
 text(s,"5",990,145,160,95,76,C.white,true,"center"); text(s,"specialized agents",930,245,280,36,23,C.white,true,"center");
 text(s,"22",990,360,160,80,60,"#D8FFF9",true,"center"); text(s,"reusable UX skills",930,447,280,36,23,C.white,true,"center");
 text(s,"Human governed · evidence traceable",72,510,600,34,20,C.aqua,true);
}

// 2 overall flow
{
 const s=p.slides.add(); s.background.fill=C.pale; title(s,"The operating model","One orchestrator routes five specialists through four human gates","The agents do the UX work. The orchestrator controls order and state. Humans control advancement.");
 const xs=[58,270,482,694,906]; const y=286;
 for(let i=0;i<4;i++) connector(s,xs[i]+164,y+72,xs[i+1]-12,y+72,C.aqua,4);
 const gates=["D1","D2","D3","D4"];
 for(let i=0;i<4;i++){shape(s,"ellipse",xs[i]+174,y+50,46,46,C.white,C.teal);text(s,gates[i],xs[i]+174,y+60,46,24,14,C.teal,true,"center");}
 const cards=[
  ["01","Discover","UX Research +\nRequirements Challenge","Evidence + BRD risk review"],
  ["02","Define & Ideate","UX Definition Agent","Problems → concepts"],
  ["03","Design & Prototype","Experience Design Agent","Flows → prototype"],
  ["04","Validate","UX Validation & Audit","Risks → coverage"],
  ["✓","Outcome","Human D4 decision","Verified prototype"]
 ];
 cards.forEach((a,i)=>{shape(s,"roundRect",xs[i],y,172,180,i===4?C.teal:C.white,i===4?"none":C.line);icon(s,a[0],xs[i]+15,y+16,i===4?C.navy:C.navy);text(s,a[1],xs[i]+18,y+82,140,48,18,i===4?C.white:C.ink,true);text(s,a[2],xs[i]+18,y+134,140,38,14,i===4?"#E3FFFB":C.muted);});
 shape(s,"roundRect",170,510,940,112,C.navy); text(s,"ORCHESTRATOR",194,532,190,24,16,C.aqua,true); text(s,"Reads state → dispatches eligible agent → validates required artifacts → stops at the next gate",395,526,680,52,20,C.white,true); text(s,"It never authors phase outputs and never approves D1–D4.",395,584,680,24,16,"#D6E7F7"); footer(s,2);
}

// 3 research
{
 const s=p.slides.add(); s.background.fill=C.white; title(s,"Agent 1 · Discover","UX Research Agent builds a trustworthy evidence baseline","It organizes what is known, what is uncertain, and what still requires research.");
 icon(s,"R",64,210,C.navy); text(s,"Evidence in",140,214,250,24,17,C.teal,true); text(s,"BRD, research notes, surveys, analytics, support tickets, stakeholder and design context",140,244,520,53,18,C.ink);
 skillRow(s,1,"Source & Evidence Analysis","Inventories every input, classifies source type, confidence, gaps and contradictions.",324);
 skillRow(s,2,"Persona Synthesis","Creates only evidence-supported personas—or fewer/limited proto-personas when evidence is weak.",406);
 skillRow(s,3,"Pain-Point Extraction","Finds traceable barriers and frustrations without converting opportunities into requirements.",488);
 sidePanel(s,"persona.md · pain-points.md · research-gaps.md → D1","Never invent demographics, quotations, motivations, behaviours or research findings.","It prevents downstream design decisions from being built on attractive but unsupported user stories."); footer(s,3);
}

// 4 requirements challenge overview
{
 const s=p.slides.add(); s.background.fill=C.pale; title(s,"Agent 2 · Discover","Requirements Challenge Agent makes the BRD argue with itself","It runs before personas so unsupported business assumptions cannot quietly become user facts.");
 // connectors first
 connector(s,252,326,456,326,C.aqua,4); connector(s,644,326,848,326,C.aqua,4);
 shape(s,"roundRect",64,228,292,210,C.navy); icon(s,"B",86,252,C.teal); text(s,"Readable BRD + source inventory",164,248,170,62,22,C.white,true); text(s,"Goals · scope · actors · workflows · constraints · assumptions",86,328,240,82,17,"#D7E8F7");
 shape(s,"roundRect",456,228,188,210,C.white,C.line); icon(s,"?",521,248,C.teal); text(s,"Requirements\nChallenge\nAgent",478,326,144,88,20,C.ink,true,"center");
 shape(s,"roundRect",848,228,360,210,C.teal); text(s,"TRACEABLE BRD RISK REVIEW",876,252,310,26,16,"#D7FFF8",true); text(s,"Strengths\nChallenged assumptions\nMissing requirements\nEdge cases & contradictions",876,300,300,116,19,C.white,true);
 text(s,"The agent does not invent the missing answer.",64,478,490,30,24,C.red,true); text(s,"A missing specification becomes a question, research gap, risk hypothesis or D1 decision—not a fabricated requirement.",64,520,1080,58,20,C.ink);
 shape(s,"roundRect",64,602,1144,49,C.navy); text(s,"Classification + confidence + source locator are required for every substantive finding.",85,614,1100,26,18,C.white,true,"center"); footer(s,4);
}

// 5 advocate cynic debate
{
 const s=p.slides.add(); s.background.fill=C.white; title(s,"Inside the challenge","Advocate, Cynic and Debate Synthesis have distinct jobs","The goal is a balanced evidence review—not a winner and loser.");
 const cols=[64,432,800]; const fills=[C.navy,"#FFF7E0",C.teal];
 const heads=["ADVOCATE REVIEW","CYNIC REVIEW","DEBATE SYNTHESIS"];
 const qs=["What is genuinely supported?","What could fail or be missing?","What should happen next?"];
 const bodies=[
  "• Stated goals and scope\n• Explicit BRD needs\n• Supported happy paths\n• Clear requirements\n• Risks already handled",
  "• Rushed-user friction\n• Failure and recovery states\n• Accessibility risks\n• Potential trust risks\n• Ambiguity and contradiction",
  "• Compares both analyses\n• Preserves contradictions\n• Classifies each finding\n• Adds confidence + source\n• Recommends actions/decisions"
 ];
 cols.forEach((x,i)=>{shape(s,"roundRect",x,220,328,338,fills[i],i===1?C.amber:"none");text(s,heads[i],x+24,244,280,26,17,i===1?C.amber:C.white,true);text(s,qs[i],x+24,286,280,54,25,i===1?C.ink:C.white,true);rule(s,x+24,353,92,i===1?C.amber:C.aqua,5);text(s,bodies[i],x+24,382,280,155,19,i===1?C.ink:C.white);});
 text(s,"Advocate does not defend assumptions.",64,590,330,26,16,C.navy,true); text(s,"Cynic does not make accusations.",432,590,330,26,16,C.amber,true); text(s,"Synthesis does not turn risk into research.",800,590,390,26,16,C.teal,true);
 shape(s,"roundRect",64,628,1128,36,C.pale);text(s,"FACT · BRD STATEMENT · INFERENCE · ASSUMPTION · RISK HYPOTHESIS    |    HIGH · MEDIUM · LOW · CONTRADICTORY",78,635,1100,22,15,C.ink,true,"center"); footer(s,5);
}

// 6 definition
{
 const s=p.slides.add(); s.background.fill=C.pale; title(s,"Agent 3 · Define & Ideate","UX Definition Agent converts evidence into a deliberate direction","It expands the solution space before recommending one concept for human review.");
 icon(s,"D",64,210,C.lav); text(s,"Approved discovery in",140,214,270,24,17,C.teal,true); text(s,"BRD risk review, personas, pain points, research gaps and supporting sources",140,244,520,48,18,C.ink);
 skillRow(s,1,"Problem Framing","Defines user, context, evidence, impact, uncertainty and business relationship.",314,C.lav);
 skillRow(s,2,"Journey Mapping","Maps stages and breakdowns; labels unsupported stages as hypothetical.",382,C.lav);
 skillRow(s,3,"Opportunity Prioritization","Ranks candidate design spaces using evidence, user value, business relevance and uncertainty.",450,C.lav);
 skillRow(s,4,"Concept Generation","Creates meaningfully different options instead of jumping to the first feature idea.",518,C.lav);
 skillRow(s,5,"Concept Evaluation","Uses common criteria to recommend a direction while preserving alternatives and risks.",586,C.lav);
 sidePanel(s,"problem · journey · opportunities · concept options · selected concept → D2","An opportunity is not a requirement, and a recommendation is not usability proof.","It converts discovery into an explainable decision rather than an unexplained solution jump."); footer(s,6);
}

// 7 design
{
 const s=p.slides.add(); s.background.fill=C.white; title(s,"Agent 4 · Design & Prototype","Experience Design Agent turns direction into testable behavior","It specifies the experience before claiming anything about its quality.");
 icon(s,"X",64,210,C.navy2); text(s,"D2-approved direction in",140,214,300,24,17,C.teal,true); text(s,"Problem, journey, opportunities, selected concept and project constraints",140,244,520,48,18,C.ink);
 skillRow(s,1,"User Flow","Maps user/system steps, decisions, alternatives, errors, recovery and exit paths.",314,C.navy2);
 skillRow(s,2,"Information Architecture","Defines hierarchy, labels and navigation when the concept genuinely needs it.",382,C.navy2);
 skillRow(s,3,"Screen Specification","Defines each screen’s purpose, content, actions, validation and traceability.",450,C.navy2);
 skillRow(s,4,"Interaction States","Covers loading, empty, error, timeout, cancellation, permission and recovery states.",518,C.navy2);
 skillRow(s,5,"Prototype Generation","Builds a prototype contract—and a runnable demo when the runtime is available.",586,C.navy2);
 sidePanel(s,"user-flow.md · screen-spec.md · interaction-states.md · prototype-spec.md → D3","Do not invent business rules, backend capabilities or unsupported product features.","It turns strategy into an inspectable experience with explicit non-happy paths—not just polished screens."); footer(s,7);
}

// 8 validation
{
 const s=p.slides.add(); s.background.fill=C.pale; title(s,"Agent 5 · Validate","Validation Agent challenges the prototype without overclaiming","Its findings are synthetic and heuristic until real research or formal testing exists.");
 icon(s,"V",64,210,C.green); text(s,"D3-approved design in",140,214,300,24,17,C.teal,true); text(s,"Persona, concept, flow, screens, interaction states, prototype and original requirements",140,244,520,48,18,C.ink);
 compactSkillRow(s,1,"Synthetic Usability Test","Simulates tasks; never claims real participants.",304,C.green);
 compactSkillRow(s,2,"Cognitive Friction Analysis","Assesses decisions and recovery with a transparent heuristic.",360,C.green);
 compactSkillRow(s,3,"Accessibility Audit","Flags evidence-bounded risks; avoids unsupported WCAG claims.",416,C.green);
 compactSkillRow(s,4,"Design-System Audit","Checks supplied system evidence—or reports NOT AVAILABLE.",472,C.green);
 compactSkillRow(s,5,"Requirement Coverage","Traces requirements through definition, design and prototype.",528,C.green);
 compactSkillRow(s,6,"Edge-Case Validation","Rechecks Phase 1 risks against designed failure states.",584,C.green);
 sidePanel(s,"validation report · issues · coverage · accessibility audit → D4","Synthetic walkthroughs are not empirical usability evidence; D4 alone can verify the prototype.","It closes the loop from BRD risk to designed behavior and exposes what remains unresolved."); footer(s,8);
}

// 9 governance recap
{
 const s=p.slides.add(); s.background.fill=C.navy; text(s,"THE GOVERNED HANDOFF",64,46,380,24,15,C.aqua,true); text(s,"Every agent narrows uncertainty—none can erase it",64,82,1120,54,38,C.white,true); text(s,"Artifacts carry evidence, assumptions, contradictions and validation needs forward. Human gates decide whether the work is ready to advance.",64,146,1100,52,20,"#D8E8F7");
 const rows=[
  ["D1","Research & requirements","Are evidence, personas, pain points and BRD challenges traceable?"],
  ["D2","Definition & direction","Is the problem framed and is the concept choice justified?"],
  ["D3","Design & prototype","Is the flow complete and the prototype ready for validation?"],
  ["D4","Final validation","Are issues understood and can the prototype be called verified within limits?"]
 ];
 rows.forEach((r,i)=>{const y=236+i*92;shape(s,"ellipse",70,y,58,58,i===3?C.teal:C.navy2,"#3C6D9E");text(s,r[0],70,y+15,58,28,18,C.white,true,"center");text(s,r[1],154,y+3,300,28,21,C.aqua,true);text(s,r[2],154,y+35,850,36,18,C.white);text(s,i===3?"VERIFY":"ADVANCE",1060,y+15,130,26,14,i===3?"#D8FFF9":"#B7D4EE",true,"center");});
 shape(s,"roundRect",64,620,1120,52,C.teal); text(s,"APPROVE advances · REVISE reruns minimum affected work · REJECT blocks",82,632,1085,28,20,C.white,true,"center");
}

await fs.mkdir(`${TMP}/rendered`,{recursive:true});
for(const [i,s] of p.slides.items.entries()){
 const stem=`slide-${String(i+1).padStart(2,"0")}`;
 const png=await p.export({slide:s,format:"png",scale:1}); await fs.writeFile(`${TMP}/rendered/${stem}.png`,new Uint8Array(await png.arrayBuffer()));
 const layout=await s.export({format:"layout"}); await fs.writeFile(`${TMP}/rendered/${stem}.layout.json`,await layout.text());
}
const pptx=await PresentationFile.exportPptx(p);
await pptx.save(`${OUT}/AI_UX_Specialized_Agent_Workflow_Guide.pptx`);
