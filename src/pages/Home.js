import { Link } from "react-router-dom";

function Home() {
    return (
        <div>
        <h1>this is where the home page will go</h1>
        <Link to="/login">log in.</Link>
        </div>
    );
  }
  
  export default Home;