// Simple script for demo link
document.getElementById('demo-link').addEventListener('click', function(e) {
    e.preventDefault();
    alert('To run the demo, start the Streamlit app with: streamlit run dashboard.py\nAnd the FastAPI server with: uvicorn api:app --reload');
});

// Add some animation to features
const features = document.querySelectorAll('#features li');
features.forEach((feature, index) => {
    feature.style.animationDelay = `${index * 0.1}s`;
    feature.style.animation = 'fadeInUp 0.5s ease-out forwards';
    feature.style.opacity = '0';
    feature.style.transform = 'translateY(20px)';
});

// CSS animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);