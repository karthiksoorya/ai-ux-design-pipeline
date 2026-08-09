const app = document.querySelector('#app');
const stepKicker = document.querySelector('#step-kicker');
const stepTitle = document.querySelector('#step-title');
const stepItems = [...document.querySelectorAll('#step-list li')];
const dialog = document.querySelector('#exit-dialog');

const initialData = () => ({
  clinic: 'Central Community Clinic', service: 'Routine consultation', date: 'Tuesday, 18 August',
  slot: '10:30 AM', role: 'self', name: '', dob: '', phone: '', email: '', reason: '',
  privacy: false, marketing: false, scenario: 'confirmed'
});
let data = initialData();
let currentStep = 1;

function setStep(step, title, html) {
  currentStep = step;
  stepKicker.textContent = `STEP ${step} OF 5`;
  stepTitle.textContent = title;
  stepItems.forEach((item, index) => {
    item.classList.toggle('active', index + 1 === step);
    item.classList.toggle('complete', index + 1 < step);
    if (index + 1 === step) item.setAttribute('aria-current', 'step'); else item.removeAttribute('aria-current');
  });
  app.innerHTML = html;
  app.focus({preventScroll:true});
}

function search() {
  setStep(1, 'Search', `
    <h3 class="section-heading">Where would you like to be seen?</h3>
    <p class="section-copy">Choose a clinic and service to view fictional appointment availability.</p>
    <div id="form-errors" class="error-summary" role="alert"></div>
    <div class="field-grid">
      <div class="field"><label for="clinic">Clinic <span class="required">*</span></label><select id="clinic"><option value="">Select a clinic</option><option selected>Central Community Clinic</option><option>Riverside Health Centre</option></select><span id="clinic-error" class="field-error"></span></div>
      <div class="field"><label for="service">Service <span class="required">*</span></label><select id="service"><option value="">Select a service</option><option selected>Routine consultation</option><option>Vaccination consultation</option></select><span id="service-error" class="field-error"></span></div>
    </div>
    <div class="button-row"><button id="search-button" type="button">View availability</button></div>`);
  document.querySelector('#search-button').addEventListener('click', () => {
    const clinic = document.querySelector('#clinic'); const service = document.querySelector('#service');
    let invalid = false;
    [[clinic,'clinic-error','Select a clinic to continue.'],[service,'service-error','Select a service to continue.']].forEach(([field,id,message]) => { const bad=!field.value; field.setAttribute('aria-invalid', String(bad)); document.querySelector('#'+id).textContent=bad?message:''; invalid ||= bad; });
    if (invalid) { document.querySelector('#form-errors').textContent='Check the highlighted fields and try again.'; (clinic.value?service:clinic).focus(); return; }
    data.clinic=clinic.value; data.service=service.value; showAvailabilityLoading();
  });
}

function showAvailabilityLoading(){
  setStep(2,'Availability',`<div class="summary-bar"><div><strong>${data.clinic}</strong><span>${data.service}</span></div></div><div class="loading-line" role="status"><span class="spinner" aria-hidden="true"></span><span>Checking fictional appointment times…</span></div>`);
  window.setTimeout(availability,650);
}

function availability() {
  setStep(2, 'Availability', `
    <div class="summary-bar"><div><strong>${data.clinic}</strong><span>${data.service}</span></div><button id="change-search" type="button">Change search</button></div>
    <h3 class="section-heading">Choose an available time</h3><p class="section-copy">Availability is communicated with text as well as visual styling.</p>
    <h4 class="date-heading">${data.date}</h4>
    <div class="slots" role="group" aria-label="Available appointment times">
      <button class="slot" type="button" data-time="9:00 AM" aria-pressed="false"><strong>9:00 AM</strong><small>✓ Available</small></button>
      <button class="slot" type="button" data-time="10:30 AM" aria-pressed="true"><strong>10:30 AM</strong><small>✓ Available</small></button>
      <button class="slot" type="button" disabled><strong>11:00 AM</strong><small>× Unavailable</small></button>
      <button class="slot" type="button" data-time="1:30 PM" aria-pressed="false"><strong>1:30 PM</strong><small>✓ Available</small></button>
      <button class="slot" type="button" data-time="3:00 PM" aria-pressed="false"><strong>3:00 PM</strong><small>✓ Available</small></button>
    </div>
    <div class="button-row"><button id="continue-details" type="button">Continue with 10:30 AM</button><button id="availability-back" class="secondary" type="button">Back</button></div>`);
  const slots=[...document.querySelectorAll('.slot:not(:disabled)')];
  slots.forEach(button=>button.addEventListener('click',()=>{ slots.forEach(x=>x.setAttribute('aria-pressed','false')); button.setAttribute('aria-pressed','true'); data.slot=button.dataset.time; document.querySelector('#continue-details').textContent=`Continue with ${data.slot}`; }));
  document.querySelector('#change-search').addEventListener('click',search); document.querySelector('#availability-back').addEventListener('click',search); document.querySelector('#continue-details').addEventListener('click',details);
}

function details() {
  setStep(3, 'Your details', `
    <div class="summary-bar"><div><strong>${data.date} at ${data.slot}</strong><span>${data.clinic} · ${data.service}</span></div><button id="change-slot" type="button">Change time</button></div>
    <h3 class="section-heading">Who is this appointment for?</h3><p class="section-copy">Caregiver authority rules are not defined in the supplied requirements.</p>
    <div class="role-options"><label class="role-card"><input type="radio" name="role" value="self" ${data.role==='self'?'checked':''}><span><strong>Myself</strong><small>I am requesting my own appointment.</small></span></label><label class="role-card"><input type="radio" name="role" value="other" ${data.role==='other'?'checked':''}><span><strong>Someone else</strong><small>Policy details require human review.</small></span></label></div>
    <div id="role-warning"></div><div id="form-errors" class="error-summary" role="alert"></div>
    <div class="field-grid">
      ${field('name','Full name','text',data.name,'Enter the full name for this request.')}
      ${field('dob','Date of birth','date',data.dob,'Enter the date of birth.')}
      ${field('phone','Phone number','tel',data.phone,'Enter a phone number.')}
      ${field('email','Email address','email',data.email,'Enter an email address.')}
      <div class="field full"><label for="reason">Reason for visit <span class="hint">Optional — do not include emergency information</span></label><textarea id="reason">${escapeHtml(data.reason)}</textarea></div>
    </div><div class="button-row"><button id="review-button" type="button">Review request</button><button id="details-back" class="secondary" type="button">Back</button></div>`);
  const updateRole=()=>{data.role=document.querySelector('input[name="role"]:checked').value;document.querySelector('#role-warning').innerHTML=data.role==='other'?'<div class="callout"><span aria-hidden="true">!</span><span>This demo does not establish caregiver authority or consent. Continue only to inspect the proposed flow.</span></div>':''};
  document.querySelectorAll('input[name="role"]').forEach(x=>x.addEventListener('change',updateRole)); updateRole();
  document.querySelector('#change-slot').addEventListener('click',availability); document.querySelector('#details-back').addEventListener('click',availability);
  document.querySelector('#review-button').addEventListener('click',validateDetails);
}

function field(id,label,type,value,message){return `<div class="field"><label for="${id}">${label} <span class="required">*</span></label><input id="${id}" type="${type}" value="${escapeHtml(value)}" required aria-describedby="${id}-error"><span id="${id}-error" class="field-error" data-message="${message}"></span></div>`}
function validateDetails(){
  const ids=['name','dob','phone','email']; let first=null;
  ids.forEach(id=>{const el=document.querySelector('#'+id);data[id]=el.value.trim();let bad=!data[id];if(id==='email'&&data[id])bad=!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data[id]);el.setAttribute('aria-invalid',String(bad));const error=document.querySelector('#'+id+'-error');error.textContent=bad?(id==='email'&&data[id]?'Enter an email address in the format name@example.com.':error.dataset.message):'';if(bad&&!first)first=el;});
  data.reason=document.querySelector('#reason').value.trim(); if(first){document.querySelector('#form-errors').textContent='Correct the highlighted fields before continuing.';first.focus();return;} review();
}

function review(){
  setStep(4,'Review',`
    <h3 class="section-heading">Review before submitting</h3><p class="section-copy">Check the fictional request and make an explicit privacy choice.</p>
    <div class="review-card"><header><h3>Appointment</h3><button id="edit-appointment" type="button">Edit</button></header><dl class="review-grid"><div><dt>Clinic</dt><dd>${data.clinic}</dd></div><div><dt>Service</dt><dd>${data.service}</dd></div><div><dt>Date</dt><dd>${data.date}</dd></div><div><dt>Time</dt><dd>${data.slot}</dd></div></dl></div>
    <div class="review-card"><header><h3>Contact details</h3><button id="edit-details" type="button">Edit</button></header><dl class="review-grid"><div><dt>Name</dt><dd>${escapeHtml(data.name)}</dd></div><div><dt>Date of birth</dt><dd>${escapeHtml(data.dob)}</dd></div><div><dt>Phone</dt><dd>${escapeHtml(data.phone)}</dd></div><div><dt>Email</dt><dd>${escapeHtml(data.email)}</dd></div></dl></div>
    <div id="form-errors" class="error-summary" role="alert"></div>
    <div class="check-row"><input id="privacy" type="checkbox" ${data.privacy?'checked':''}><label for="privacy"><strong>I accept the privacy notice <span class="required">*</span></strong><br><span class="hint">Required to submit this synthetic request.</span></label></div>
    <div class="check-row"><input id="marketing" type="checkbox" ${data.marketing?'checked':''}><label for="marketing"><strong>Send optional marketing updates</strong><br><span class="hint">Optional and unselected by default.</span></label></div>
    <div class="scenario-box"><label for="scenario">Simulated outcome for demonstration</label><select id="scenario"><option value="confirmed">Confirmed</option><option value="pending">Pending</option><option value="stale">Slot no longer available</option><option value="rejected">Request rejected</option><option value="timeout">Outcome unknown / timeout</option><option value="unavailable">Service unavailable</option><option value="partial">Confirmed; email delivery failed</option></select><span class="hint">This control demonstrates proposed UI states, not backend behaviour.</span></div>
    <div class="button-row"><button id="submit-request" type="button">Submit request once</button><button id="review-back" class="secondary" type="button">Back</button></div>`);
  document.querySelector('#scenario').value=data.scenario; document.querySelector('#edit-appointment').addEventListener('click',availability); document.querySelector('#edit-details').addEventListener('click',details); document.querySelector('#review-back').addEventListener('click',details);
  document.querySelector('#submit-request').addEventListener('click',()=>{data.privacy=document.querySelector('#privacy').checked;data.marketing=document.querySelector('#marketing').checked;data.scenario=document.querySelector('#scenario').value;if(!data.privacy){document.querySelector('#form-errors').textContent='Privacy notice: select the required checkbox before submitting.';document.querySelector('#privacy').focus();return;}processing();});
}

function processing(){setStep(5,'Submitting request',`<div class="loading-line" role="status"><span class="spinner" aria-hidden="true"></span><div><strong>Submitting the fictional request once…</strong><p>Controls are locked to avoid duplicate activation.</p></div></div>`);window.setTimeout(outcome,700)}
function outcome(){
  const outcomes={
    confirmed:{kind:'success',icon:'✓',title:'Appointment confirmed',body:`Your fictional appointment is confirmed for ${data.date} at ${data.slot}.`,detail:'Reference DEMO-2048'},
    pending:{kind:'warning',icon:'…',title:'Not yet confirmed',body:'The request is pending. Do not treat this as a confirmed appointment.',detail:'Reference DEMO-2048'},
    stale:{kind:'warning',icon:'!',title:'That time is no longer available',body:'The selected slot changed before submission. Choose another available time.',detail:null},
    rejected:{kind:'error',icon:'×',title:'Request not confirmed',body:'This synthetic request was not accepted. No unsupported reason is inferred.',detail:null},
    timeout:{kind:'warning',icon:'?',title:'Outcome unknown',body:'The response timed out. Do not assume the request succeeded or submit automatically again.',detail:null},
    unavailable:{kind:'error',icon:'!',title:'Service temporarily unavailable',body:'The request could not be completed. No appointment has been confirmed.',detail:null},
    partial:{kind:'success',icon:'✓',title:'Appointment confirmed',body:'The booking is confirmed, but simulated email delivery failed. Keep the on-screen reference.',detail:'Reference DEMO-2048'}
  }; const o=outcomes[data.scenario];
  setStep(5,'Request outcome',`<div class="status-card ${o.kind}" role="status"><span class="status-icon" aria-hidden="true">${o.icon}</span><h3>${o.title}</h3><p>${o.body}</p>${o.detail?`<span class="reference">${o.detail}</span>`:''}</div><div class="button-row">${data.scenario==='stale'?'<button id="return-slots" type="button">View refreshed availability</button>':''}<button id="restart" class="secondary" type="button">Start a new request</button></div>`);
  document.querySelector('#restart').addEventListener('click',()=>{data=initialData();search()});const slots=document.querySelector('#return-slots');if(slots)slots.addEventListener('click',availability);
}

function escapeHtml(value){return String(value).replace(/[&<>'"]/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[char]))}
function openExit(){dialog.hidden=false;document.querySelector('#stay').focus()} function closeExit(){dialog.hidden=true;document.querySelector('#exit-button').focus()}
document.querySelector('#exit-button').addEventListener('click',openExit);document.querySelector('#stay').addEventListener('click',closeExit);document.querySelector('.dialog-close').addEventListener('click',closeExit);document.querySelector('#confirm-exit').addEventListener('click',()=>{data=initialData();dialog.hidden=true;search()});dialog.addEventListener('click',event=>{if(event.target===dialog)closeExit()});document.addEventListener('keydown',event=>{if(event.key==='Escape'&&!dialog.hidden)closeExit()});

search();
