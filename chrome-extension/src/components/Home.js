import React, {useState} from "react";
import {Link, useNavigate} from 'react-router-dom';
import Logo from "../assets/news.png";

function Home() {
  const [summaryString, setSummaryString] = useState("");
  const navigate = useNavigate();


  window.summaryString = "";
  // Function to handle the button click and make a request to the Express server
  const handleRequest = async () => {
    try {
      const url = await getCurrentTabUrl();
      console.log("Current Tab URL:", url);

      const response = await fetch("http://localhost:3000/api/hello", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: url }),
      });

      const data = await response.json();
      console.log(data); // Handle the response data

      setSummaryString(data.output); //Summary stored here
      navigate("/article-summary", {state: {summary: data.output}});
    } catch (error) {
      console.error("Error:", error); // Handle errors
    }
  };

  async function getCurrentTabUrl() {
    return new Promise((resolve, reject) => {
      let queryOptions = { active: true, lastFocusedWindow: true };
      chrome.tabs.query(queryOptions, (tabs) => {
        let tab = tabs[0];
        if (tab) {
          resolve(tab.url);
        } else {
          reject("No active tab found");
        }
      });
    });
  }

  return (
    <div>
      <div className="bg-gradient flex items-center justify-center h-screen">
        <div className="flex flex-col items-center">
          <img
            src={Logo}
            className="mb-4 w-56 h-auto animate-scale-up-down"
            alt="Logo"
          />
          <h1 className="text-4xl font-poppins text-white font-bold">
            [Title]
          </h1>
          <Link to="/main-page">
            <button
              className="button"
              style={{ marginTop: "30px" }}
              onClick={handleRequest}
            >
              Analyze Article
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Home;
