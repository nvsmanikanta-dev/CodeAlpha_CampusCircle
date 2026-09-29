(() => {
  const modal = document.getElementById('createModal');
  const open = () => {
    if (!modal) return;
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');
    modal.querySelector('textarea')?.focus();
  };
  const close = () => {
    if (!modal) return;
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-open');
  };
  document.querySelectorAll('[data-open-create]').forEach(button => button.addEventListener('click', open));
  document.querySelectorAll('[data-close-create]').forEach(button => button.addEventListener('click', close));
  document.addEventListener('keydown', event => { if (event.key === 'Escape') close(); });
  document.querySelectorAll('[data-focus-comment]').forEach(button => button.addEventListener('click', () => document.getElementById(button.dataset.focusComment)?.focus()));
  document.querySelectorAll('[data-confirm-delete]').forEach(form => form.addEventListener('submit', event => { if (!window.confirm('Delete this post?')) event.preventDefault(); }));
})();
