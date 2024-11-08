function createMatrixEffect() {
    const body = document.querySelector("body");
    const matrixContainer = document.createElement("div");
    matrixContainer.classList.add("matrix-column");
    body.appendChild(matrixContainer);

    for (let i = 0; i < 100; i++) {
        const matrixText = document.createElement("div");
        matrixText.classList.add("matrix-text");
        matrixText.textContent = String.fromCharCode(0x30A0 + Math.random() * 96);
        matrixText.style.position = "absolute";
        matrixText.style.top = `${Math.random() * 100}%`;
        matrixText.style.left = `${Math.random() * 100}%`;
        matrixText.style.animationDelay = `${Math.random() * 5}s`;
        matrixText.style.animationDuration = `${1.5 + Math.random()}s`; // variație în viteză
        matrixContainer.appendChild(matrixText);
    }
}
