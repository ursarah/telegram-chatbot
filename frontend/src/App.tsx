
import logo from "./assets/logo.png"
const App = () => {
  const handleRedirect = () => {
    window.open("https://t.me/FuriaTCSBot", "_blank")
  }
  return (
    <div className="bg-[#ffffffc4] max-w-md mx-auto p-4 space-y-4 rounded-md shadow-2xs">
      <h1 className="text-center">Chat Furia</h1>
      <div className="text-center">
        <h1>Entrar em conversa pelo telegram</h1>
        <img src={logo} alt="telegram" className="w-[30%] mx-auto my-5" />
        <button className="bg-blue-400 py-2 px-6 rounded-2xl cursor-pointer" onClick={handleRedirect}>Entrar</button>
      </div>
    </div>
  )
}

export default App