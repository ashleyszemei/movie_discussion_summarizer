import React from 'react';
import './App.css';
import SummarySection from './components/Summary';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>r/movies Movie Discussion Summarizer</h1>
      </header>
      <main>
        <SummarySection />
      </main>
    </div>
  );
};

export default App;