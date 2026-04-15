function loadLogs() {
    fetch("/logs")
        .then(response => response.json())
        .then(data => {
            let logs = data.logs.split("\n");

            let formatted = logs.map(line => {
                if (line.includes("[Key.enter]")) return "⏎ ENTER";
                if (line.includes("[Key.space]")) return "␣ SPACE";
                if (line.includes("[Key.backspace]")) return "⌫ BACKSPACE";
                if (line.includes("[Key.shift")) return "⇧ SHIFT";
                if (line.includes("[Key.ctrl")) return "CTRL";

                return line;
            }).join("\n");

            document.getElementById("output").textContent = formatted;
        });
}setInterval(loadLogs, 3000);