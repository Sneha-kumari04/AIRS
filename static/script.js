async function analyze() {
    const file = document.getElementById("resumeFile").files[0];
    const job = document.getElementById("job").value.trim();

    if (!file || !job) {
        alert("Resume file aur Job Description dono required hain.");
        return;
    }

    const btn = document.getElementById("analyzeBtn");
    const loader = document.getElementById("loader");
    const resultBox = document.getElementById("result-box");
    const errorBox = document.getElementById("error-box");

    btn.disabled = true;
    btn.innerText = "Analyzing...";
    loader.style.display = "block";
    resultBox.style.display = "none";
    errorBox.style.display = "none";

    try {
        const formData = new FormData();
        formData.append("resume", file);
        formData.append("job", job);

        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        const result = data.result;

        const score = result.match_score;
        const scoreEl = document.getElementById("score-value");
        scoreEl.innerText = score + "%";

        // Color code score
        if (score >= 70) {
            scoreEl.style.color = "#10b981"; 
        } else if (score >= 40) {
            scoreEl.style.color = "#f59e0b"; 
        } else {
            scoreEl.style.color = "#ef4444"; 
        }

        document.getElementById("verdict-value").innerText = result.verdict;

        populateList("matched-skills", result.matched_skills);
        populateList("missing-skills", result.missing_skills);
        populateList("improvement-tips", result.improvement_tips);

        // Show result box
        resultBox.style.display = "block";

    } catch (error) {
        errorBox.style.display = "block";
        document.getElementById("error-msg").innerText = error.message || "Something went wrong.";
        console.error(error);

    } finally {
        btn.disabled = false;
        btn.innerText = "Analyze Resume";
        loader.style.display = "none";
    }
}


function populateList(elementId, items) {
    const ul = document.getElementById(elementId);
    ul.innerHTML = "";

    if (!items || items.length === 0) {
        ul.innerHTML = "<li>None found</li>";
        return;
    }

    items.forEach(item => {
        const li = document.createElement("li");
        li.innerText = item;
        ul.appendChild(li);
    });
}