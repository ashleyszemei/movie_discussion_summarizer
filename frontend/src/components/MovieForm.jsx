import React, { useState } from 'react';

const MovieForm = ({ generateSummary }) => {
  const [url, resetUrl] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (url) {
      generateSummary(url);
      resetUrl('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={url}
        onChange={(e) => resetUrl(e.target.value)}
        placeholder="Enter URL"
      />
      <button type="submit">Generate Summary</button>
    </form>
  );
};

export default MovieForm;