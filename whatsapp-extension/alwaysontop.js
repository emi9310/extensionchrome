document.addEventListener('DOMContentLoaded', function() {
    var alwaysOnTopButton = document.getElementById('always-on-top');
  
    alwaysOnTopButton.addEventListener('click', function() {
      chrome.runtime.sendMessage({ command: 'activateAlwaysOnTop' });
    });
  });
  