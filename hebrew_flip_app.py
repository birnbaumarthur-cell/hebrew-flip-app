<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible Text Fetcher & Flipper</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Noto+Sans+Hebrew:wght@400;700&display=swap');
        
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6;
        }
        .hebrew-text {
            font-family: 'Noto Sans Hebrew', sans-serif;
            direction: rtl;
            white-space: pre-wrap; 
            line-height: 1.6;
        }
        .reversed-text {
            font-family: 'Noto Sans Hebrew', sans-serif;
            direction: ltr; 
            text-align: right;
            white-space: pre-wrap; 
            line-height: 1.6;
            unicode-bidi: bidi-override;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col items-center py-10 px-4">

    <div class="w-full max-w-3xl bg-white rounded-xl shadow-lg overflow-hidden">
        
        <!-- Header -->
        <div class="bg-indigo-600 p-6 text-white text-center">
            <h1 class="text-2xl font-bold"><i class="fas fa-book-open mr-2"></i>Bible Text Fetcher</h1>
            <p class="text-indigo-100 text-sm mt-1">Clean Sefaria text for Adobe Illustrator</p>
            <a href="https://www.alephbeta.org" target="_blank" class="text-indigo-200 hover:text-white text-xs mt-2 inline-block font-medium transition">alephbeta.org</a>
        </div>

        <!-- Controls -->
        <div class="p-6 border-b border-gray-100">
            <!-- Input Area -->
            <div class="flex flex-col sm:flex-row gap-3 mb-6">
                <div class="flex-grow">
                    <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Citation</label>
                    <input type="text" id="citationInput" placeholder="e.g., Numbers 30:2, Genesis 1:1" 
                        class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-indigo-500 outline-none transition text-lg"
                        onkeypress="handleEnter(event)">
                </div>
                <div class="flex items-end">
                    <button onclick="fetchText()" id="fetchBtn"
                        class="w-full sm:w-auto bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-8 py-2.5 rounded-lg transition shadow-sm flex items-center justify-center gap-2">
                        <i class="fas fa-search"></i> Fetch
                    </button>
                </div>
            </div>

            <!-- Filters -->
            <div class="bg-gray-50 p-4 rounded-lg border border-gray-200 flex flex-wrap gap-6 justify-center sm:justify-start">
                <div class="flex items-center">
                    <input type="checkbox" id="stripVowels" class="mr-2 h-4 w-4 text-indigo-600 rounded focus:ring-indigo-500" onchange="processText()">
                    <label for="stripVowels" class="text-sm text-gray-700 font-medium">Remove Vowels (Niqqud)</label>
                </div>
                <div class="flex items-center">
                    <input type="checkbox" id="stripCantillation" class="mr-2 h-4 w-4 text-indigo-600 rounded focus:ring-indigo-500" checked onchange="processText()">
                    <label for="stripCantillation" class="text-sm text-gray-700 font-medium">Remove Trop (Cantillation)</label>
                </div>
            </div>
            
            <div id="errorMsg" class="hidden mt-4 text-center bg-red-50 text-red-600 text-sm font-medium p-3 rounded-lg">
                <i class="fas fa-exclamation-circle mr-1"></i> <span id="errorText"></span>
            </div>
        </div>

        <!-- Results Area -->
        <div class="p-6 grid grid-cols-1 md:grid-cols-2 gap-6 bg-white">
            
            <!-- Original Column (Primary) -->
            <div class="flex flex-col">
                <div class="flex justify-between items-center mb-2">
                    <h3 class="font-bold text-gray-800 flex items-center gap-2">
                        <span class="w-2 h-2 bg-green-500 rounded-full"></span> Original (Standard)
                    </h3>
                    <span class="text-[10px] text-gray-400 uppercase tracking-wider font-bold">Use This</span>
                </div>
                <div class="relative flex-grow">
                    <textarea id="originalOutput" readonly 
                        class="hebrew-text w-full h-48 p-4 border-2 border-green-100 focus:border-green-300 rounded-xl bg-green-50/30 text-xl resize-none focus:outline-none transition"></textarea>
                </div>
                <button onclick="copyToClipboard('originalOutput')" 
                    class="mt-3 w-full bg-green-600 hover:bg-green-700 text-white py-2 rounded-lg transition shadow-sm flex items-center justify-center gap-2 font-medium">
                    <i class="far fa-copy"></i> Copy Standard Text
                </button>
            </div>

            <!-- Flipped Column (Secondary/Backup) -->
            <div class="flex flex-col opacity-90 hover:opacity-100 transition">
                <div class="flex justify-between items-center mb-2">
                    <h3 class="font-bold text-gray-500 flex items-center gap-2">
                        <span class="w-2 h-2 bg-gray-300 rounded-full"></span> Flipped (Legacy)
                    </h3>
                    <span class="text-[10px] text-gray-400 uppercase tracking-wider font-bold">Backup</span>
                </div>
                <div class="relative flex-grow">
                    <textarea id="flippedOutput" readonly 
                        class="reversed-text w-full h-48 p-4 border border-gray-200 rounded-xl bg-gray-50 text-xl resize-none focus:outline-none text-gray-600"></textarea>
                </div>
                <button onclick="copyToClipboard('flippedOutput')" 
                    class="mt-3 w-full bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 py-2 rounded-lg transition shadow-sm flex items-center justify-center gap-2 text-sm">
                    <i class="fas fa-exchange-alt"></i> Copy Flipped
                </button>
            </div>
        </div>

        <!-- English Translation Section -->
        <div class="px-6 pb-6">
             <div class="border-t border-gray-100 pt-4">
                <h3 class="text-xs font-bold text-gray-400 uppercase mb-2">English Translation</h3>
                <p id="englishOutput" class="text-gray-600 text-sm italic bg-white p-3 border border-gray-100 rounded-lg min-h-[3rem]">
                    ...
                </p>
             </div>
        </div>

    </div>

    <div class="mt-8 text-center text-gray-400 text-xs max-w-lg">
        <p>Powered by <a href="https://www.sefaria.org" target="_blank" class="underline hover:text-gray-600">Sefaria API</a>.</p>
    </div>

    <script>
        let rawHebrew = "";
        let rawEnglish = "";

        function handleEnter(e) {
            if (e.key === 'Enter') fetchText();
        }

        async function fetchText() {
            const citation = document.getElementById('citationInput').value.trim();
            const btn = document.getElementById('fetchBtn');
            const errorDiv = document.getElementById('errorMsg');
            
            if (!citation) return;

            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            btn.disabled = true;
            errorDiv.classList.add('hidden');

            try {
                const response = await fetch(`https://www.sefaria.org/api/texts/${citation}?context=0`);
                if (!response.ok) throw new Error("Citation not found or API error.");
                
                const data = await response.json();
                if (data.error) throw new Error(data.error);

                const joinText = (content) => Array.isArray(content) ? content.join("\n") : (content || "");
                rawHebrew = joinText(data.he);
                rawEnglish = joinText(data.text);

                if (!rawHebrew) throw new Error("No Hebrew text found for this citation.");

                processText();

                // Update English
                let cleanEnglish = rawEnglish.replace(/<br\s*\/?>/gi, '\n').replace(/<\/p>/gi, '\n');
                let tmpDiv = document.createElement("DIV");
                tmpDiv.innerHTML = cleanEnglish;
                document.getElementById('englishOutput').innerHTML = (tmpDiv.textContent || tmpDiv.innerText || "").replace(/\n/g, '<br>');

            } catch (err) {
                errorDiv.classList.remove('hidden');
                document.getElementById('errorText').innerText = err.message;
                rawHebrew = "";
                document.getElementById('originalOutput').value = "";
                document.getElementById('flippedOutput').value = "";
                document.getElementById('englishOutput').innerText = "...";
            } finally {
                btn.innerHTML = '<i class="fas fa-search"></i> Fetch';
                btn.disabled = false;
            }
        }

        function processText() {
            if (!rawHebrew) return;

            let text = stripHtmlPreservingLines(rawHebrew);
            text = text.replace(/[\u200E\u200F\u202A-\u202E]/g, ""); // Remove invisible directional marks
            text = text.replace(/\u200D/g, ""); // Remove Zero Width Joiners

            const stripVowels = document.getElementById('stripVowels').checked;
            const stripCantillation = document.getElementById('stripCantillation').checked;

            if (stripCantillation) text = text.replace(/[\u0591-\u05AF]/g, ""); 
            if (stripVowels) text = text.replace(/[\u05B0-\u05BD\u05BF\u05C1\u05C2\u05C4\u05C5\u05C7]/g, "");

            document.getElementById('originalOutput').value = text;

            // Method B (Classic) hardcoded
            const lines = text.split('\n');
            const flippedLines = lines.map(line => fixBrackets(line.split('').reverse().join('')));

            document.getElementById('flippedOutput').value = flippedLines.join('\n');
        }

        function fixBrackets(text) {
            return text.replace(/[()\[\]{}]/g, function(c) {
                if (c === '(') return ')'; if (c === ')') return '(';
                if (c === '[') return ']'; if (c === ']') return '[';
                if (c === '{') return '}'; if (c === '}') return '{';
                return c;
            });
        }

        function stripHtmlPreservingLines(html) {
            let processed = html.replace(/<br\s*\/?>/gi, '\n').replace(/<\/p>/gi, '\n');
            let tmp = document.createElement("DIV");
            const SAFE_NEWLINE = "###SAFE_NEWLINE_TOKEN###";
            processed = processed.replace(/\r?\n/g, SAFE_NEWLINE);
            tmp.innerHTML = processed;
            let cleanText = tmp.textContent || tmp.innerText || "";
            return cleanText.split(SAFE_NEWLINE).join('\n');
        }

        function copyToClipboard(elementId) {
            const copyText = document.getElementById(elementId);
            copyText.select();
            copyText.setSelectionRange(0, 99999);
            try {
                document.execCommand("copy");
                
                // Button feedback logic
                const btn = document.querySelector(`button[onclick="copyToClipboard('${elementId}')"]`);
                if (btn) {
                    const originalContent = btn.innerHTML;
                    btn.innerHTML = '<i class="fas fa-check"></i> Copied!';
                    btn.classList.add('bg-gray-800', 'text-white'); // Generic active state
                    setTimeout(() => {
                        btn.innerHTML = originalContent;
                        btn.classList.remove('bg-gray-800', 'text-white');
                    }, 2000);
                }
            } catch (err) { alert("Failed to copy text"); }
        }
    </script>
</body>
</html>
