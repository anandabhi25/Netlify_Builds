const motionQuery = matchMedia('(prefers-reduced-motion: reduce)');
const io = new IntersectionObserver(entries => entries.forEach(entry => {
  if (entry.isIntersecting) {
    entry.target.classList.add('on');
    io.unobserve(entry.target);
  }
}), {threshold: .08});
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
const bar = document.querySelector('.progress span');
let ticking = false;
function updateProgress() {
  const root = document.documentElement;
  const range = root.scrollHeight - root.clientHeight;
  bar.style.width = `${range > 0 ? Math.min(100, Math.max(0, root.scrollTop / range * 100)) : 0}%`;
  ticking = false;
}
addEventListener('scroll', () => {
  if (!ticking) { ticking = true; requestAnimationFrame(updateProgress); }
}, {passive: true});
addEventListener('resize', updateProgress);
updateProgress();
document.querySelectorAll('a[href^="#"]').forEach(anchor => anchor.addEventListener('click', event => {
  const target = document.getElementById(anchor.getAttribute('href').slice(1));
  if (target) {
    event.preventDefault();
    target.scrollIntoView({behavior: motionQuery.matches ? 'instant' : 'smooth'});
    history.replaceState(null, '', anchor.getAttribute('href'));
  }
}));
