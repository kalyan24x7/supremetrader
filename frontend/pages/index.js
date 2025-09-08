import { useState, useEffect } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [items, setItems] = useState([]);

  const fetchHello = async () => {
    const res = await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + "/hello");
    const data = await res.json();
    setMessage(data.message);
  };

  useEffect(() => {
    async function loadItems() {
      const res = await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + "/items");
      const data = await res.json();
      setItems(data);
    }
    loadItems();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Hello World App</h1>
      <button onClick={fetchHello}>Say Hello</button>
      <p>{message}</p>
      <h2>Items in DB:</h2>
      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}