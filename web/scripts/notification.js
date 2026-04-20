function showNotification(message, type = 'info') {
    // 移除旧的
    const old = document.querySelector('.notification');
    if (old) old.remove();

    const div = document.createElement('div');
    div.className = `notification notification-${type}`;
    div.textContent = message;
    document.body.appendChild(div);

    // 触发 reflow
    requestAnimationFrame(() => div.classList.add('show'));

    // 根据类型设置不同的显示时间
    // 错误消息通常更重要，显示时间稍长
    const duration = (type === 'error' || type === 'success') ? 4000 : 2500;
    
    setTimeout(() => {
        div.classList.remove('show');
        setTimeout(() => div.remove(), 400);
    }, duration);
}