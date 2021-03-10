from shared_modules.logger import get_logger


def handler(event, context):
    get_logger().log_handler_enter(event, context)

    return """
		<script type=\"text/javascript\">
			function getParameterByName(name, url) {
			    if (!url) url = window.location.href;
			    name = name.replace(/[\[\]]/g, \"\\$&\");
			    var regex = new RegExp(\"[?&]\" + name + \"(=([^&#]*)|&|#|$)\"),
			        results = regex.exec(url);
			    if (!results) return null;
			    if (!results[2]) return '';
			    return decodeURIComponent(results[2].replace(/\+/g, \" \"));
			}
			document.addEventListener(\"DOMContentLoaded\", function(event) {
				var gclid = getParameterByName(\"gclid\", window.location.href);
				if(gclid) {
					var utmSource = 'Google';
					var utmMedium = 'Adwords';
				} else {
					var utmSource = getParameterByName(\"utm_source\", window.location.href);
					var utmMedium = getParameterByName(\"utm_medium\", window.location.href);
				}
				if(document.referrer) {
				var referralURL = document.referrer;
					if(referralURL.includes(\"google\")){
						createCookie('referral-source','google');
						if (utmMedium === \"\" || utmMedium === null) {
							utmMedium = 'organic';
							createCookie('utm-medium',utmMedium);
						}
						createCookie('utm-medium',utmMedium);
					}else if(referralURL.includes(\"facebook\")){
						createCookie('referral-source','facebook');
					}else if(referralURL.includes(\"yelp\")){
						createCookie('referral-source','yelp');
					}
				}
				var referralSource = getCookie('referral-source');
				if(utmSource === \"\" || utmSource === null){
					utmSource = referralSource;
					if(referralSource === \"google\"){
						utmMedium = getCookie('utm-medium');
					} else if(referralSource === \"facebook\"){
						utmMedium = \"social\";
					} else if(referralSource === \"yelp\"){
						utmMedium = \"local\";
					}
				}
				try{
					// check if the incoming traffic is from referral and if data exists in DNI
					if(utmSource !== null && utmMedium !== null && dniData.dniDictionary.length){
						// run the dniDictionary
						for(var i = 0; i < dniData.dniDictionary.length; i++){
							if(dniData.dniDictionary[i].utm_source.toLowerCase() === utmSource.toLowerCase() && dniData.dniDictionary[i].utm_medium.toLowerCase() === utmMedium.toLowerCase()){
								// check if phone number exists regardless for pattern
								var dniPattern = /(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})/gm;
								var match, results=[];
								do {
									match = dniPattern.exec(document.body.innerHTML);
									if (match) {
										results.push(match[1]);
									}
								} while (match);
								// if number exists then verify the document.body number with the search number in dictionary
								if(results.length){
									for(var j = 0; j < results.length; j++){
										// unmask the number from document.body and DNI's search number
										var numberInContent = results[j].replace(/\D+/g,'');
										var unmaskedSearchNumber = dniData.dniDictionary[i].searchNumber.replace(/\D+/g,'');
										// if number matches with search number then replace the number
										if(numberInContent === unmaskedSearchNumber){
											// unmask DNI replace number and add xxx xxx xxxx masking
											var dniReplaceNumber = dniData.dniDictionary[i].replaceNumber.replace(/[^\d]+/g, '').replace(/(\d{3})(\d{3})(\d{4})/, '$1-$2-$3');
											document.body.innerHTML = document.body.innerHTML.split(results[j]).join(dniReplaceNumber);
										}
									}
								}
							}
						}
					}
				} catch(error){
					console.log(\"An Error occured: \", error);
				}
			});
			function getCookie(cookie_name) {
			    var name = cookie_name + \"=\";
			    var decodedCookie = decodeURIComponent(document.cookie);
			    var cookies = decodedCookie.split(';');
			    for(var i = 0; i < cookies.length; i++) {
			        var cookie_param = cookies[i];
			        while (cookie_param.charAt(0) == ' ') {
			           cookie_param = cookie_param.substring(1);
			        }
			        if (cookie_param.indexOf(name) == 0) {
			            return cookie_param.substring(name.length, cookie_param.length);
			        }
			    }
			    return '';
			}
			function createCookie(name,value,minutes) { //Default cookie expired time
				minutes = minutes || 30;
			    var date = new Date();
			    date.setTime(date.getTime()+(minutes * 60 * 1000));
			    var expires = '; expires='+date.toGMTString();
			    document.cookie = name+'='+value+expires;
			}
		</script>"""
