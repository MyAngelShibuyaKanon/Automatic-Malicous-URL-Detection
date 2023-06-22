chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    if (tab.active && change.url) {
        console.log("you are here: "+change.url);

        fetch("http://localhost:5000/post", {
            method: 'POST',
            headers: {
                'url': change.url
            }
        });   
    }
});