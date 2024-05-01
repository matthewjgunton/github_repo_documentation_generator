

async function getGitData() {

  function getGitCommits() {
    // Find all the elements that represent added or deleted lines of code
    const additions = document.querySelectorAll('.blob-code-addition');
    const deletions = document.querySelectorAll('.blob-code-deletion');

    // Initialize arrays to hold the content of these lines
    const addedLines = [];
    const deletedLines = [];

    // Iterate over additions and extract the text
    additions.forEach(addition => {
        // Ensure to get only the content relevant to the code change
        const codeContent = addition.querySelector('.blob-code-inner');
        if (codeContent) {
            addedLines.push(codeContent.textContent);
        }
    });

    // Iterate over deletions and extract the text
    deletions.forEach(deletion => {
        // Ensure to get only the content relevant to the code change
        const codeContent = deletion.querySelector('.blob-code-inner');
        if (codeContent) {
            deletedLines.push(codeContent.textContent);
        }
    });

    // Return an object containing both arrays of added and deleted lines
    return {
        addedLines,
        deletedLines
    };
  }

  function getFilename() {
    var fileNameElement = document.querySelector('.Link--primary.Truncate-text');
    // Check if the element exists to avoid errors
    if (fileNameElement) {
      console.log(fileNameElement.textContent)
      // Return the text content of the element which is the file name
      return fileNameElement.textContent;
    } else {
      console.log("ELSE");
      // Return a message if the element is not found
      return 'File name not found.';
    }
  }

  let fileName = getFilename();
  let gitCommits = getGitCommits();

  let data = fileName+": added lines: ["+gitCommits.addedLines + "]. removed lines: ["+gitCommits.deletedLines+"]";
  console.log("REACHED END OF Fn", data);
  return "Read the following git change ```"+data+"``` Give a summary of the change.";
}

async function callLLM (text) {
  console.log("text: ", text);
  const val = await callOpenAIGPT35Turbo(text);
  console.log("RES: ",val);
  return val;
}

async function callOpenAIGPT35Turbo(promptText) {
    const endpoint = 'https://api.openai.com/v1/chat/completions'; // GPT-3.5-turbo endpoint

    const data = {
        model: "gpt-3.5-turbo",
        messages: [{
            role: "user",
            content: promptText
        }]
    };

    const response = await fetch( endpoint , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${OPENAI_API_KEY}`
        },
        body: JSON.stringify(data)
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result =  await response.json();
    return result.choices[0].message.content;
}

async function callAnthropic(data) {
    const requestOptions = {
        method: 'POST',
        headers: {
          'x-api-key': ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          model: 'claude-3-haiku-20240307',
          max_tokens: 1024,
          messages: [
            { role: 'user', content: 'Hello, world' }
          ]
        })
      };
      
      // Make the fetch request
      return await fetch('https://cors-anywhere.herokuapp.com/https://api.anthropic.com/v1/messages', requestOptions)
}

async function writeResponse(value){
  var textArea = document.getElementById('pull_request_body');
  textArea.value = value;
}

async function test() {
  console.log("HIT");
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs)=>{
    console.log(tabs[0]);
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      func: getGitData
    }, (prompt) => {
      console.log("REACHED PROMPT", prompt);
      callLLM(prompt[0].result).then(result=>{
        //#pull_request_body
        console.log("RESULT REACHED UP", result);
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          func: writeResponse,
          args: [result]
        })
      });
    });
  });
}

async function fetchData() {
  test();
  const date = new Date();
  var year = date.getFullYear();
  var month = date.getMonth();
  var day = date.getDate();

  var lastMidnight = new Date(year, month, day).getTime();
  var $table = $('#table');
  const data = await chrome.history.search(
    {
      text: '', // Return every history item....
      startTime: lastMidnight
    })

  let dataString = "";
  data.forEach(function(item) {
      dataString += "<tr>";
      var $newRow = $('<tr>');
      $newRow.append($('<td>').text(item.url));
      dataString += "<td>"+item.url+"</td>";
      $newRow.append($('<td>').text(item.title));
      dataString += "<td>"+item.title+"</td>";
      $table.append($newRow);
      dataString += "</tr>";
  });
  const prompt = "Read the below web browser history, and then give a summary of what the user worked on today. Please write in the first person.```"+dataString+"```";
  // const response = await callLLM(prompt);
  // console.log("API: ", response);

}
fetchData();
