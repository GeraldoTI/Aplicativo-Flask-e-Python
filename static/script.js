document.getElementById('tagForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const tagInput = document.getElementById('tagInput');
    const tag = tagInput.value;

    fetch('/add_tag', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ tag: tag })
    })
    .then(response => response.json())
    .then(data => {
        tagInput.value = ''; // Limpa o campo de entrada
        updateTagList(data); // Atualiza a lista de tags
    });
});

function updateTagList(tags) {
    const tagList = document.getElementById('tagList');
    tagList.innerHTML = ''; // Limpa a lista existente

    tags.forEach(tag => {
        const li = document.createElement('li');
        li.className = 'list-group-item';
        li.textContent = tag;
        tagList.appendChild(li);
    });
}
