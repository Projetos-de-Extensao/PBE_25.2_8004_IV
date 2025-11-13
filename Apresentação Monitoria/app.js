document.addEventListener('DOMContentLoaded', () => {
    // Adiciona rolagem suave para os links da navbar
    document.querySelectorAll('.navbar a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault(); // Previne o comportamento padrão do link

            const targetId = this.getAttribute('href'); // Pega o ID da seção alvo
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                // Rola para a seção de forma suave
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});