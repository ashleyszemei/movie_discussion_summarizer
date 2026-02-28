import React, { useEffect, useState } from 'react';
import MovieForm from './MovieForm';
import api from '../api';
import Spinner from './spinner';
import MovieCard from './MovieCard';

import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: (theme.vars ?? theme).palette.text.secondary,
  ...theme.applyStyles('dark', {
    backgroundColor: '#1A2027',
  }),
}));

const SummarySection = () => {
  const [movies, setMovies] = useState([]);
  const [summary, showSummary] = useState('');
  const [url, setUrl] = useState('');
  const [isLoadingMov, setIsLoadingMov] = useState(true);
  const [isLoadingSumm, setIsLoadingSumm] = useState(false);

  const loadMovies = async(url) => {
    api.get('/movies')
    .then(function(response) {
      setIsLoadingMov(false);
      setMovies(response.data.movies);
    })
    .catch(function(response) {
      setIsLoadingMov(false);
      console.error("Error loading movies", error);
    })
  };

  const generateSummary = async (url) => {
    showSummary('');
    setIsLoadingSumm(true);
    
    api.post('/summarize', { url: url })
    .then(function(response) {
      setIsLoadingSumm(false);
      showSummary(response.data.summary);
    })
    .catch(function(error) {
      setIsLoadingSumm(false);
      console.error("Error generating summary", error);
    })
  };

  const handleClick = (event) => {
    event.preventDefault();
    const url = event.currentTarget.getAttribute('url');
    setUrl(url);
  };

  useEffect(() => {
    loadMovies();
  }, []);

  return (
    <div>
      <div className="page-section">
        { isLoadingMov && <Spinner text="Loading movies..."/>}
        <Grid container spacing={2}>
          {movies.map((movie, index) => (
            <Grid key={index} size={3}>
              <MovieCard 
                url={movie.url}
                title={movie.title}
                poster_url={movie.poster_url}
                onClick={handleClick}/>
            </Grid>
          ))}
        </Grid>
      </div>
      <div className="page-section">
        <MovieForm generateSummary={generateSummary} url={url} />
      </div>
      <div className="page-section">
        { isLoadingSumm && <Spinner text="Loading summary..."/>}
        <div className="summary-section">
          {/* <p>{summary}</p> */}
          <div dangerouslySetInnerHTML={{__html: summary}}></div>
        </div>
      </div>
    </div>
  );
};

export default SummarySection;