import React, { useEffect, useState } from 'react';
import MovieForm from './MovieForm';
import api from '../api';
import Spinner from './spinner';

const SummarySection = () => {
  const [summary, showSummary] = useState([]);
  const [isPending, setIsPending] = useState(false);

  const generateSummary = async (url) => {
    setIsPending(true);
    
    api.post('/summarize', { url: url })
    .then(function(response) {
      setIsPending(false);
      showSummary(response.data.summary);
    })
    .catch(function(error) {
      setIsPending(false);
      console.error("Error generating summary", error);
    })
  };

  useEffect(() => {
    
  }, []);

  return (
    <div>
      <MovieForm generateSummary={generateSummary} />
      { isPending && <Spinner text="Loading..."/>}
      <p className='summary'>{summary}</p>
    </div>
  );
};

export default SummarySection;