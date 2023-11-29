const visitCounter = document.querySelector('.visitCount');
async function updateCounter() {
  let response = await fetch("https://kfz3syi2sco53vdnzuzzeforue0dbeqj.lambda-url.eu-west-2.on.aws/");
  let data = await response.json();
  visitCounter.innerHTML = `${data}`;
}

updateCounter();