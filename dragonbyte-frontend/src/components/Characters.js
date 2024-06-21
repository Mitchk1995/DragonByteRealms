// src/components/Characters.js
import React, { useEffect, useState } from 'react';
import api from '../api';

const Characters = ({ token }) => {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    const fetchCharacters = async () => {
      try {
        const response = await api.get('characters/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setCharacters(response.data);
      } catch (error) {
        console.error('Failed to fetch characters', error);
      }
    };

    if (token) {
      fetchCharacters();
    }
  }, [token]);

  return (
    <div>
      <h2>Characters</h2>
      <ul>
        {characters.map((character) => (
          <li key={character.id}>{character.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Characters;
