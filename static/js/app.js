document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('[data-track]').forEach(el=>el.addEventListener('click',()=>{if(typeof gtag==='function'){gtag('event','cta_click',{cta_name:el.dataset.track})}}));
  const chart=document.getElementById('sourceChart');
  if(chart){
    const dataNode=document.getElementById('dashboard-data'); const rows=dataNode?JSON.parse(dataNode.textContent):[];
    new Chart(chart,{type:'bar',data:{labels:rows.map(r=>r.source),datasets:[{label:'Website visits (demo)',data:rows.map(r=>r.visits),borderWidth:1}]},options:{responsive:true,plugins:{legend:{display:false}},scales:{y:{beginAtZero:true}}}});
  }
});
