import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';

export default function OutlinedCard(props) {
  return (
    <Box sx={{ minWidth: 275 }}>
            <Card variant="outlined" className="movie-card" onClick={props.onClick} url={props.url}>
                <React.Fragment>
                    <CardMedia
                      sx={{ 
                        height: 400,
                        backgroundPosition: 'center'
                       }}
                      image={props.poster_url}
                      title={props.title}
                    />
                </React.Fragment>
            </Card>
    </Box>
  );
}