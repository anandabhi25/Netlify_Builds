
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('on')}),{threshold:.15});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const bar=document.querySelector('.progress span');
addEventListener('scroll',()=>{const h=document.documentElement;const p=h.scrollTop/(h.scrollHeight-h.clientHeight);bar.style.width=(p*100)+'%'});
document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{const t=document.querySelector(a.getAttribute('href'));if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth'})}}));
