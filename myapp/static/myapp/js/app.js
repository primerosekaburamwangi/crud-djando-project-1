"use strict";

const searchInput = document.querySelector("[data-user-search]");
const userCards = Array.from(document.querySelectorAll("[data-user-card]"));
const noSearchResults = document.querySelector("[data-no-results]");

if (searchInput && userCards.length) {
    searchInput.addEventListener("input", () => {
        const query = searchInput.value.trim().toLocaleLowerCase();
        let visibleCount = 0;

        userCards.forEach((card) => {
            const matches = card.dataset.search.toLocaleLowerCase().includes(query);
            card.hidden = !matches;
            if (matches) {
                visibleCount += 1;
            }
        });

        if (noSearchResults) {
            noSearchResults.hidden = visibleCount > 0;
        }
    });
}

if (searchInput) {
    document.addEventListener("keydown", (event) => {
        const target = event.target;
        const isTyping = target instanceof HTMLElement
            && (target.isContentEditable || ["INPUT", "TEXTAREA", "SELECT"].includes(target.tagName));
        if (event.key === "/" && !isTyping && !event.ctrlKey && !event.metaKey && !event.altKey) {
            event.preventDefault();
            searchInput.focus();
        }
    });
}

const photoInput = document.querySelector("#id_photo");
const photoPreview = document.querySelector("[data-photo-preview]");

if (photoInput && photoPreview) {
    let previewUrl = null;

    photoInput.addEventListener("change", () => {
        const [file] = photoInput.files;
        if (!file) {
            return;
        }

        if (previewUrl) {
            URL.revokeObjectURL(previewUrl);
        }
        previewUrl = URL.createObjectURL(file);
        photoPreview.src = previewUrl;
    });
}
