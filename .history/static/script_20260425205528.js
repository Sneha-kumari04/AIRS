async function analyze() {
    const file = document.getElementById("resumeFile").files[0];
    const job = document.getElementById("job").value;

    if (!file || !job) {
        alert("Upload resume and fill job description");
        return;
    }

    let formData = new FormData();
    formData.append("resume", file);
    formData.append("job", job);

    const resultBox = document.getElementById("result");
    resultBox.innerText = "Analyzing...";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();
        resultBox.innerText = data.result;

    } catch (error) {
        resultBox.innerText = "Something went wrong. Check server.";
        console.error(error);
    }
}