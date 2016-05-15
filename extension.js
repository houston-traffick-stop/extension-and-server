document.addEventListener('DOMContentLoaded', function(){
	var checkbutton = document.getElementById('checkpage');
	checkbutton.addEventListener('click', function () {
		chrome.tabs.getSelected(null, function(tab){		
			var f = document.createElement('form');
			f.action = 'http://localhost:5000/submit';
			f.method = 'post';
			var i = document.createElement('input');
			i.type = 'hidden';
			i.name = 'url';
			i.value = tab.url;
			f.appendChild(i);
			document.body.appendChild(f);
			f.submit();
		});
	}, false);
},false);
