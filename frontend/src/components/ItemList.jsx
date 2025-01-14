import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ItemList = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/items/')
            .then(response => setItems(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <ul>
            {items.map(item => (
                <li key={item.id}>
                    <h3>{item.name}</h3>
                    <p>{item.description}</p>
                </li>
            ))}
        </ul>
    );
};

export default ItemList;
