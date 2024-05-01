import { useRef, useEffect, useState } from 'react';

export default function App() {
  const [timeLeft, setTimeLeft] = useState(3);
  const interval = useRef<number>(0);

  useEffect(() => {
    interval.current = window.setInterval(() => {
      // Decrease "timeLeft" by 1 every second
      setTimeLeft((prev) => prev - 1);
    }, 1000);

    return () => window.clearInterval(interval.current);
  }, []);

  useEffect(() => {
    // Open the link in a new tab when the countdown ends
    if (timeLeft === 0) {
      window.clearInterval(interval.current);

      // 👇 Open link in new tab programmatically
      window.open('https://codingbeautydev.com', '_blank', 'noreferrer');
    }
  }, [timeLeft]);

  return (
    <div>
      The link will open in <b>{timeLeft}</b> second(s)
    </div>
  );
}