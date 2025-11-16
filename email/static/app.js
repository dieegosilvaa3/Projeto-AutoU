const formulario = document.getElementById("formularioEmail");
const resultado = document.getElementById("resultado");
const categoriaEl = document.getElementById("categoria");
const confiancaEl = document.getElementById("confianca");
const respostaEl = document.getElementById("resposta");
const sinaisEl = document.getElementById("sinais");
const inputArquivo = document.getElementById("arquivo");
const nomeArquivo = document.getElementById("arquivo_nome");
const botaoLimpar = document.getElementById("botaoLimpar");

botaoLimpar.addEventListener("click", () => {
  formulario.reset();
  nomeArquivo.textContent = "Nenhum arquivo escolhido";
  resultado.classList.add("oculto");
});

inputArquivo.addEventListener("change", () => {
  if (inputArquivo.files.length > 0) {
    nomeArquivo.textContent = inputArquivo.files[0].name;
  } else {
    nomeArquivo.textContent = "Nenhum arquivo escolhido";
  }
});

function copiarTexto() {
  const texto = respostaEl.textContent; 
  navigator.clipboard.writeText(texto).then(() => {
    alert("Copiado!");
  });
}

formulario.addEventListener("submit", async (e) => {
  e.preventDefault();
  const fd = new FormData(formulario);

  const respostajson = await fetch("/processar", { method: "POST", body: fd });
  const dados = await respostajson.json();

  if (!respostajson.ok) {
    alert(dados.error || "Erro ao processar.");
    return;
  }
  
  categoriaEl.textContent = dados.categoria;
  confiancaEl.textContent = dados.confianca;
  respostaEl.textContent = dados.resposta;
  sinaisEl.textContent = JSON.stringify(dados.sinais, null, 2);

  resultado.classList.remove("oculto");
});