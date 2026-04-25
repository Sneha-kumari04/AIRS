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

    document.getElementById("result").innerText = "Analyzing...";

    const response = await fetch("/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.result;
}