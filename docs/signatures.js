/* SAPfans.io signatures — EgD-SAPF-009. A connecting point, not a forum.
   Sign -> pick LinkedIn, X or GitHub. LinkedIn/X: tick Experience and/or Questions, then post on your own
   profile with the item's hashtag; nothing is stored here, peers find you by hashtag search.
   GitHub: the signature form records your public GitHub account (scripts/sign.py -> docs/signatures.json). */
(function(){
var FORM="https://github.com/EVEglyphDesign/sapfans-io/issues/new?template=signature.yml";
var IC={
 linkedin:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 110-4.13 2.06 2.06 0 010 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>',
 x:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>',
 github:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .3a12 12 0 00-3.8 23.38c.6.12.82-.26.82-.58v-2.04c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73 1.2.09 1.84 1.24 1.84 1.24 1.07 1.83 2.81 1.3 3.49 1 .11-.78.42-1.3.76-1.6-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.13-.3-.54-1.52.12-3.18 0 0 1-.32 3.3 1.23a11.5 11.5 0 016 0c2.28-1.55 3.29-1.23 3.29-1.23.66 1.66.25 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.61-2.81 5.62-5.48 5.92.43.37.81 1.1.81 2.22v3.29c0 .32.22.7.83.58A12 12 0 0012 .3"/></svg>'
};
var NAME={linkedin:"LinkedIn",x:"X",github:"GitHub"};
var TAG={"L-SAP":"SAPfansBDC","L-AWS":"SAPfansAWS","L-MICROSOFT":"SAPfansMicrosoft","L-GOOGLE":"SAPfansGoogle","L-PALANTIR":"SAPfansPalantir"};
var R={};
function esc(t){return String(t==null?"":t).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function tagOf(id){return TAG[id]||("SAPfans"+String(id).replace(/[^A-Za-z0-9]/g,""))}
function form(id){return FORM+"&title="+encodeURIComponent("Sign "+id)+"&ref="+encodeURIComponent(id)+"&action=Sign"}
function text(label,id,e,q,url,why){var s=e&&q?"I have experience with "+label+" and questions about it.":e?"I have experience with "+label+".":"I have questions about "+label+".";
  return s+(why?" Why it matters: "+why:"")+" Open to connecting with peers."+(url?"\n"+url:"")+"\nhttps://sapfans.io/#"+id+"\n#SAPfans #"+tagOf(id)}
function post(net,t){return net==="x"?"https://x.com/intent/post?text="+encodeURIComponent(t):"https://www.linkedin.com/feed/?shareActive=true&text="+encodeURIComponent(t)}
function find(net,id){var h=encodeURIComponent("#"+tagOf(id));return net==="x"?"https://x.com/search?q="+h+"&f=live":"https://www.linkedin.com/search/results/content/?keywords="+h}
function tg(a){a=String(a||"").toLowerCase();var e=a.indexOf("experience")>=0,q=a.indexOf("question")>=0;return e&&q?"Both":e?"Experience":q?"Questions":""}
function block(id){
 var who=R[id]||[],n=who.length;
 var list=n?'<ul class="sig-list" hidden>'+who.map(function(p){return '<li><span class="sig-n">'+esc(p.name)+'</span>'+Object.keys(p.links).map(function(k){return ' <a href="'+esc(p.links[k])+'" target="_blank" rel="noopener nofollow ugc" data-net="'+k+'" title="'+esc(p.name)+' on '+NAME[k]+'">'+IC[k]+'<span class="egd-sr">'+NAME[k]+'</span></a>'}).join("")+(tg(p.as)?' <span class="sig-t">'+tg(p.as)+'</span>':'')+'</li>'}).join("")+'</ul>':"";
 var findl='<span class="sig-find"><span>Who signed:</span> <a href="'+find("linkedin",id)+'" target="_blank" rel="noopener">LinkedIn</a> · <a href="'+find("x",id)+'" target="_blank" rel="noopener">X</a> · '+(n?'<button type="button" class="sig-who">GitHub ('+n+')</button>':'<span>GitHub (0)</span>')+'</span>';
 var pick='<div class="sig-pick" hidden>'+["linkedin","x","github"].map(function(net){return '<button type="button" class="sig-b" data-net="'+net+'" title="'+NAME[net]+'">'+IC[net]+'<span class="egd-sr">'+NAME[net]+'</span></button>'}).join("")+'</div>'+
  '<div class="sig-step" hidden><label><input type="checkbox" value="e"> <span>Experience</span></label><label><input type="checkbox" value="q"> <span>Questions</span></label><a class="sig-post" aria-disabled="true" target="_blank" rel="noopener">Post</a></div>'+
  '<div class="sig-gh" hidden><a class="sig-go" href="'+form(id)+'" target="_blank" rel="noopener">Continue on GitHub</a></div><p class="sig-msg" hidden></p>';
 return '<div class="sig-row"><button type="button" class="sig-go sig-start">Sign</button>'+findl+'</div>'+pick+list}
function paint(){document.querySelectorAll(".sig[data-ref]").forEach(function(el){el.innerHTML=block(el.dataset.ref)})}
function upd(sg){var st=sg.querySelector(".sig-step"),a=st.querySelector(".sig-post"),c=st.querySelectorAll("input"),e=c[0].checked,q=c[1].checked;
  if(e||q){var t=text(sg.dataset.label||sg.dataset.ref,sg.dataset.ref,e,q,sg.dataset.url,sg.dataset.net==="x"?"":sg.dataset.why);a.href=post(sg.dataset.net,t);a.dataset.t=t;a.removeAttribute("aria-disabled")}else{a.removeAttribute("href");a.setAttribute("aria-disabled","true")}}
document.addEventListener("change",function(e){var sg=e.target.closest(".sig");if(sg&&e.target.closest(".sig-step"))upd(sg)});
document.addEventListener("click",function(e){
 var t=e.target,sg=t.closest(".sig");if(!sg)return;
 if(t.closest(".sig-start")){var pk=sg.querySelector(".sig-pick");pk.hidden=!pk.hidden;sg.classList.toggle("on",!pk.hidden);if(pk.hidden){["sig-step","sig-gh","sig-msg"].forEach(function(c){sg.querySelector("."+c).hidden=true})}return}
 var b=t.closest(".sig-b");if(b&&b.tagName==="BUTTON"){var net=b.dataset.net;sg.dataset.net=net;
   sg.querySelectorAll(".sig-b").forEach(function(x){x.classList.toggle("on",x===b)});
   sg.querySelector(".sig-step").hidden=net==="github";sg.querySelector(".sig-gh").hidden=net!=="github";sg.querySelector(".sig-msg").hidden=true;
   if(net!=="github"){var a=sg.querySelector(".sig-post");a.textContent="Post on "+NAME[net];upd(sg)}return}
 var p=t.closest(".sig-post");if(p&&p.dataset.t&&!p.hasAttribute("aria-disabled")){try{navigator.clipboard.writeText(p.dataset.t)}catch(_){}
   var m=sg.querySelector(".sig-msg");m.hidden=false;m.textContent="Your post opens on "+NAME[sg.dataset.net]+". The text is also copied, in case it opens empty: paste and post.";return}
 var w=t.closest(".sig-who");if(w){var l=sg.querySelector(".sig-list");if(l)l.hidden=!l.hidden}});
window.egdSig={paint:paint};
fetch("signatures.json",{cache:"no-cache"}).then(function(r){return r.json()}).then(function(j){R=j.refs||{};paint()}).catch(paint);
})();
