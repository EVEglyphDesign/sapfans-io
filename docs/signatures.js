/* SAPfans.io signatures — EgD-SAPF-009. A connecting point, not a forum.
   Each reference card carries three buttons: LinkedIn · X · GitHub. Pressing one opens a prefilled
   GitHub form; the repo's workflow records the signer (scripts/sign.py -> docs/signatures.json). */
(function(){
var FORM="https://github.com/EVEglyphDesign/sapfans-io/issues/new?template=signature.yml";
var IC={
 linkedin:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 110-4.13 2.06 2.06 0 010 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>',
 x:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>',
 github:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .3a12 12 0 00-3.8 23.38c.6.12.82-.26.82-.58v-2.04c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73 1.2.09 1.84 1.24 1.84 1.24 1.07 1.83 2.81 1.3 3.49 1 .11-.78.42-1.3.76-1.6-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.13-.3-.54-1.52.12-3.18 0 0 1-.32 3.3 1.23a11.5 11.5 0 016 0c2.28-1.55 3.29-1.23 3.29-1.23.66 1.66.25 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.61-2.81 5.62-5.48 5.92.43.37.81 1.1.81 2.22v3.29c0 .32.22.7.83.58A12 12 0 0012 .3"/></svg>'
};
var NAME={linkedin:"LinkedIn",x:"X",github:"GitHub"};
var R={};
function esc(t){return String(t==null?"":t).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
var AS={e:"Experience",q:"Questions",eq:"Experience and questions"};
function href(id,net,as){return FORM+"&title="+encodeURIComponent("Sign "+id)+"&ref="+encodeURIComponent(id)+"&net="+NAME[net]+(as?"&as="+encodeURIComponent(AS[as]):"")+"&action=Sign"}
function tag(a){a=String(a||"").toLowerCase();var e=a.indexOf("experience")>=0,q=a.indexOf("question")>=0;return e&&q?"Both":e?"Experience":q?"Questions":""}
function block(id){
 var who=R[id]||[],n=who.length;
 var b=["linkedin","x","github"].map(function(net){
  return '<button type="button" class="sig-b" data-net="'+net+'" title="Sign with your '+NAME[net]+'">'+IC[net]+'<span class="egd-sr">'+NAME[net]+'</span></button>'}).join("");
 var step='<div class="sig-step" hidden><label><input type="checkbox" value="e"> <span>Experience</span></label><label><input type="checkbox" value="q"> <span>Questions</span></label><a class="sig-go" aria-disabled="true" target="_blank" rel="noopener" data-ref="'+esc(id)+'">Sign</a></div>';
 var list=n?'<ul class="sig-list" hidden>'+who.map(function(p){return '<li><span class="sig-n">'+esc(p.name)+'</span>'+Object.keys(p.links).map(function(k){return ' <a href="'+esc(p.links[k])+'" target="_blank" rel="noopener nofollow ugc" data-net="'+k+'" title="'+esc(p.name)+' on '+NAME[k]+'">'+IC[k]+'<span class="egd-sr">'+NAME[k]+'</span></a>'}).join("")+(tag(p.as)?' <span class="sig-t">'+tag(p.as)+'</span>':'')+'</li>'}).join("")+'</ul>':"";
 var ne=who.filter(function(p){return /experience/i.test(p.as||"")}).length,nq=who.filter(function(p){return /question/i.test(p.as||"")}).length;
 var c=n?'<button type="button" class="sig-who"><b>'+ne+'</b> <span>with experience</span> · <b>'+nq+'</b> <span>with questions</span> · <span>see who</span></button>':'<span class="sig-none">Found it useful? Leave your signature.</span>';
 return '<div class="sig-row">'+b+c+'</div>'+step+list}
function paint(){document.querySelectorAll(".sig[data-ref]").forEach(function(el){el.innerHTML=block(el.dataset.ref)})}
function upd(st){var v=[].slice.call(st.querySelectorAll("input:checked")).map(function(i){return i.value}).join(""),g=st.querySelector(".sig-go");
 if(v){g.href=href(g.dataset.ref,st.dataset.net,v);g.removeAttribute("aria-disabled")}else{g.removeAttribute("href");g.setAttribute("aria-disabled","true")}}
document.addEventListener("change",function(e){var st=e.target.closest(".sig-step");if(st)upd(st)});
document.addEventListener("click",function(e){var b=e.target.closest(".sig-b");if(b&&b.tagName==="BUTTON"){var sg=b.closest(".sig"),st=sg.querySelector(".sig-step");
  sg.querySelectorAll(".sig-b").forEach(function(x){x.classList.toggle("on",x===b)});st.dataset.net=b.dataset.net;st.hidden=false;upd(st);return}
 var w=e.target.closest(".sig-who");if(!w)return;var l=w.closest(".sig").querySelector(".sig-list");if(l)l.hidden=!l.hidden});
window.egdSig={paint:paint};
fetch("signatures.json",{cache:"no-cache"}).then(function(r){return r.json()}).then(function(j){R=j.refs||{};paint()}).catch(paint);
})();
