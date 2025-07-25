document.getElementById("suggestBtn").addEventListener("click", async () => {
    const modalContent = document.getElementById("modalContent");
    modalContent.textContent = "Loading book...";
    const res = await fetch("/api/book/suggest");
    const data = await res.json();
    if (data.error) {
        modalContent.textContent = data.error;
    } else {
        modalContent.innerHTML = `
            <strong>Title:</strong> ${data.title}<br>
            <strong>Author:</strong> ${data.author}<br>
            <strong>Genre:</strong> ${data.genre}
        `;
    }
});