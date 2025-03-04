async function analyzeComments() {
    const videoUrl = document.getElementById("video-url").value;

    if (!videoUrl || !videoUrl.includes("youtube.com/watch?v=")) {
        alert("Please enter a valid YouTube video URL.");
        return;
    }

    document.getElementById("results").innerHTML = "Analyzing comments...";

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ video_url: videoUrl })
        }); 

        const data = await response.json();

        displayResults(data);
    } catch (error) {
        console.error("Error analyzing comments:", error);
        document.getElementById("results").innerHTML = "An error occurred. Please try again.";
    }
}

function displayResults(comments) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = ""; 
    if (comments.length === 0) {
        resultsDiv.innerHTML = "<p>No comments found.</p>";
        return;
    }

    comments.forEach(commentData => {
        const commentDiv = document.createElement("div");
        commentDiv.classList.add("comment");

        if (commentData.analysis.includes("negative")) {
            commentDiv.classList.add("negative");
        }
        if (commentData.analysis.includes("controversial")) {
            commentDiv.classList.add("controversial");
        }

        commentDiv.innerHTML = `
            <strong>Comment:</strong> ${commentData.comment}<br>
            <strong>Analysis:</strong> ${commentData.analysis}
        `;

        resultsDiv.appendChild(commentDiv);
    });
}