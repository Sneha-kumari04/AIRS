async function analyze() {
    const resume = document.getElementById("resume").value;
    const job = document.getElementById("job").value;

    if (!resume || !job) {
        alert("Please fill both fields");
        return;
    }

    document.getElementById("result").innerText = "Processing...";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ resume, job })
        });

        const data = await response.json();

        document.getElementById("result").innerText = data.result;

    } catch (error) {
        document.getElementById("result").innerText = "Error occurred";
        console.error(error);
    }
}