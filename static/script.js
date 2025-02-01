// Remova esta linha:
// import games from "./games.json";
const colors = {
  steam: "#1b2838",
  epic: "#313131",
  gog: "#6E4295",
};

async function fetchGames() {
  const response = await fetch("./static/games.json");
  const games = await response.json();
  return games;
}

function Card({ title, img, origin }) {
  return (
    <div className="card" style={{ "--main-color": colors[origin] }}>
      <div className="card-image">
        <img src={img} alt={title} />
      </div>
      <div className="card-info">
        <h3>{title}</h3>
        <span className="origin-node">{origin.toUpperCase()}</span>
      </div>
    </div>
  );
}

function App() {
  const [games, setGames] = React.useState([]);

  React.useEffect(() => {
    fetchGames().then(setGames);
  }, []);

  return (
    <main>
      <h1>My Game List</h1>
      <section className="cards">
        {games.map((game) => (
          <Card
            key={game.id}
            title={game.name}
            img={game.image}
            origin={game.origin}
          />
        ))}
      </section>
    </main>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
