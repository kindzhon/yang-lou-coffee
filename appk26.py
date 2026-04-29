import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="洋语楼咖啡 | YangYuLou Coffee",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern artistic style
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .stApp {
        background: linear-gradient(135deg, #f5f0eb 0%, #ede6de 50%, #e8ddd1 100%);
        font-family: 'Noto Serif SC', serif;
    }

    /* Navigation */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(245, 240, 235, 0.92);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(139, 90, 43, 0.1);
        padding: 0 5%;
        transition: all 0.4s ease;
    }

    .nav-inner {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 0;
    }

    .nav-logo {
        font-family: 'Playfair Display', serif;
        font-size: 1.6rem;
        font-weight: 600;
        color: #5c3a1e;
        letter-spacing: 3px;
        text-decoration: none;
    }

    .nav-logo span {
        font-size: 0.8rem;
        display: block;
        letter-spacing: 5px;
        color: #8b7355;
        font-weight: 400;
        margin-top: 2px;
    }

    .nav-links {
        display: flex;
        gap: 40px;
        list-style: none;
    }

    .nav-links a {
        text-decoration: none;
        color: #6b4423;
        font-size: 0.95rem;
        font-weight: 400;
        letter-spacing: 1px;
        position: relative;
        padding: 5px 0;
        transition: color 0.3s ease;
    }

    .nav-links a::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 1.5px;
        background: #8b5a2b;
        transition: width 0.4s ease;
    }

    .nav-links a:hover::after {
        width: 100%;
    }

    .nav-links a:hover {
        color: #8b5a2b;
    }

    /* Hero Section */
    .hero-section {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        padding: 120px 5% 80px;
    }

    .hero-bg-pattern {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        opacity: 0.04;
        background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%235c3a1e' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    }

    .hero-content {
        max-width: 1400px;
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
        position: relative;
        z-index: 1;
    }

    .hero-text {
        animation: fadeInUp 1s ease-out;
    }

    .hero-subtitle {
        font-family: 'Playfair Display', serif;
        font-size: 0.9rem;
        letter-spacing: 6px;
        color: #a08060;
        text-transform: uppercase;
        margin-bottom: 20px;
    }

    .hero-title {
        font-family: 'Noto Serif SC', serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #3d2314;
        line-height: 1.3;
        margin-bottom: 25px;
    }

    .hero-title .highlight {
        color: #8b5a2b;
        position: relative;
    }

    .hero-desc {
        font-size: 1.1rem;
        color: #7a6655;
        line-height: 2;
        margin-bottom: 40px;
        max-width: 480px;
    }

    .hero-btn {
        display: inline-block;
        padding: 16px 45px;
        background: #5c3a1e;
        color: #f5f0eb;
        text-decoration: none;
        font-size: 0.95rem;
        letter-spacing: 3px;
        border-radius: 50px;
        transition: all 0.4s ease;
        border: 2px solid #5c3a1e;
    }

    .hero-btn:hover {
        background: transparent;
        color: #5c3a1e;
    }

    .hero-btn-secondary {
        display: inline-block;
        padding: 16px 45px;
        background: transparent;
        color: #5c3a1e;
        text-decoration: none;
        font-size: 0.95rem;
        letter-spacing: 3px;
        border-radius: 50px;
        border: 2px solid #5c3a1e;
        margin-left: 15px;
        transition: all 0.4s ease;
    }

    .hero-btn-secondary:hover {
        background: #5c3a1e;
        color: #f5f0eb;
    }

    .hero-visual {
        position: relative;
        height: 550px;
        animation: fadeIn 1.2s ease-out 0.3s both;
    }

    .hero-image-main {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 20px;
        box-shadow: 0 30px 60px rgba(92, 58, 30, 0.15);
    }

    .hero-float-card {
        position: absolute;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 20px 25px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(92, 58, 30, 0.1);
    }

    .float-card-1 {
        bottom: 40px;
        left: -30px;
        animation: float 3s ease-in-out infinite;
    }

    .float-card-2 {
        top: 30px;
        right: -20px;
        animation: float 3s ease-in-out 1.5s infinite;
    }

    .float-card-icon {
        font-size: 1.8rem;
        margin-bottom: 8px;
    }

    .float-card-text {
        font-size: 0.85rem;
        color: #6b4423;
        font-weight: 600;
    }

    .float-card-sub {
        font-size: 0.75rem;
        color: #a08060;
        margin-top: 3px;
    }

    /* Section Styles */
    .section {
        padding: 100px 5%;
        position: relative;
    }

    .section-header {
        text-align: center;
        margin-bottom: 70px;
    }

    .section-label {
        font-family: 'Playfair Display', serif;
        font-size: 0.85rem;
        letter-spacing: 5px;
        color: #a08060;
        text-transform: uppercase;
        margin-bottom: 15px;
    }

    .section-title {
        font-family: 'Noto Serif SC', serif;
        font-size: 2.5rem;
        font-weight: 600;
        color: #3d2314;
        margin-bottom: 15px;
    }

    .section-desc {
        font-size: 1rem;
        color: #7a6655;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.8;
    }

    /* Story Section */
    .story-grid {
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 60px;
        align-items: center;
    }

    .story-image {
        position: relative;
    }

    .story-image img {
        width: 100%;
        height: 450px;
        object-fit: cover;
        border-radius: 20px;
        box-shadow: 0 20px 50px rgba(92, 58, 30, 0.12);
    }

    .story-image::before {
        content: '';
        position: absolute;
        top: -20px;
        left: -20px;
        width: 100%;
        height: 100%;
        border: 2px solid #c4a882;
        border-radius: 20px;
        z-index: -1;
    }

    .story-content h3 {
        font-family: 'Noto Serif SC', serif;
        font-size: 2rem;
        color: #3d2314;
        margin-bottom: 25px;
        font-weight: 600;
    }

    .story-content p {
        font-size: 1rem;
        color: #7a6655;
        line-height: 2;
        margin-bottom: 20px;
    }

    .story-stats {
        display: flex;
        gap: 40px;
        margin-top: 35px;
    }

    .stat-item h4 {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        color: #8b5a2b;
        font-weight: 600;
    }

    .stat-item p {
        font-size: 0.85rem;
        color: #a08060;
        margin-top: 5px;
    }

    /* Products Section */
    .products-section {
        background: linear-gradient(180deg, #f5f0eb 0%, #ebe3d9 100%);
    }

    .products-grid {
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 35px;
    }

    .product-card {
        background: #fff;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(92, 58, 30, 0.08);
        transition: all 0.4s ease;
        position: relative;
    }

    .product-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 50px rgba(92, 58, 30, 0.15);
    }

    .product-image {
        width: 100%;
        height: 280px;
        object-fit: cover;
        transition: transform 0.6s ease;
    }

    .product-card:hover .product-image {
        transform: scale(1.05);
    }

    .product-badge {
        position: absolute;
        top: 20px;
        left: 20px;
        background: #8b5a2b;
        color: #fff;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.75rem;
        letter-spacing: 1px;
        font-weight: 600;
    }

    .product-info {
        padding: 28px;
    }

    .product-category {
        font-size: 0.8rem;
        color: #a08060;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .product-name {
        font-family: 'Noto Serif SC', serif;
        font-size: 1.3rem;
        color: #3d2314;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .product-desc {
        font-size: 0.9rem;
        color: #7a6655;
        line-height: 1.7;
        margin-bottom: 20px;
    }

    .product-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .product-price {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        color: #8b5a2b;
        font-weight: 600;
    }

    .product-price span {
        font-size: 0.9rem;
        color: #a08060;
        text-decoration: line-through;
        margin-left: 8px;
    }

    .add-cart-btn {
        background: #5c3a1e;
        color: #fff;
        border: none;
        padding: 10px 24px;
        border-radius: 25px;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.3s ease;
        letter-spacing: 1px;
    }

    .add-cart-btn:hover {
        background: #8b5a2b;
        transform: scale(1.05);
    }

    /* Features Section */
    .features-grid {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 30px;
    }

    .feature-card {
        text-align: center;
        padding: 40px 25px;
        background: rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(139, 90, 43, 0.08);
        transition: all 0.4s ease;
    }

    .feature-card:hover {
        background: rgba(255, 255, 255, 0.9);
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(92, 58, 30, 0.1);
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 20px;
    }

    .feature-title {
        font-family: 'Noto Serif SC', serif;
        font-size: 1.1rem;
        color: #3d2314;
        font-weight: 600;
        margin-bottom: 12px;
    }

    .feature-desc {
        font-size: 0.85rem;
        color: #7a6655;
        line-height: 1.7;
    }

    /* Gallery Section */
    .gallery-grid {
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(2, 250px);
        gap: 15px;
    }

    .gallery-item {
        border-radius: 16px;
        overflow: hidden;
        position: relative;
        cursor: pointer;
    }

    .gallery-item img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s ease;
    }

    .gallery-item:hover img {
        transform: scale(1.1);
    }

    .gallery-item.large {
        grid-column: span 2;
        grid-row: span 2;
    }

    .gallery-item.wide {
        grid-column: span 2;
    }

    .gallery-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 25px;
        background: linear-gradient(transparent, rgba(61, 35, 20, 0.8));
        color: #fff;
        opacity: 0;
        transition: opacity 0.4s ease;
    }

    .gallery-item:hover .gallery-overlay {
        opacity: 1;
    }

    .gallery-overlay h4 {
        font-family: 'Noto Serif SC', serif;
        font-size: 1.1rem;
        margin-bottom: 5px;
    }

    .gallery-overlay p {
        font-size: 0.8rem;
        opacity: 0.8;
    }

    /* Testimonials */
    .testimonials-grid {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
    }

    .testimonial-card {
        background: #fff;
        padding: 40px 30px;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(92, 58, 30, 0.06);
        position: relative;
    }

    .testimonial-card::before {
        content: '"';
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        color: #c4a882;
        position: absolute;
        top: 10px;
        left: 25px;
        line-height: 1;
        opacity: 0.4;
    }

    .testimonial-text {
        font-size: 0.95rem;
        color: #5a4a3a;
        line-height: 1.9;
        margin-bottom: 25px;
        position: relative;
        z-index: 1;
    }

    .testimonial-author {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .author-avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        object-fit: cover;
    }

    .author-info h5 {
        font-family: 'Noto Serif SC', serif;
        font-size: 1rem;
        color: #3d2314;
        font-weight: 600;
    }

    .author-info p {
        font-size: 0.8rem;
        color: #a08060;
        margin-top: 2px;
    }

    .stars {
        color: #c4a882;
        font-size: 1rem;
        margin-bottom: 15px;
    }

    /* Newsletter / CTA */
    .cta-section {
        background: linear-gradient(135deg, #5c3a1e 0%, #3d2314 100%);
        padding: 100px 5%;
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .cta-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.03) 1px, transparent 1px);
        background-size: 30px 30px;
    }

    .cta-content {
        position: relative;
        z-index: 1;
        max-width: 700px;
        margin: 0 auto;
    }

    .cta-title {
        font-family: 'Noto Serif SC', serif;
        font-size: 2.5rem;
        color: #f5f0eb;
        font-weight: 600;
        margin-bottom: 20px;
    }

    .cta-desc {
        font-size: 1.05rem;
        color: rgba(245, 240, 235, 0.7);
        line-height: 1.8;
        margin-bottom: 40px;
    }

    .cta-form {
        display: flex;
        gap: 15px;
        justify-content: center;
        max-width: 500px;
        margin: 0 auto;
    }

    .cta-input {
        flex: 1;
        padding: 16px 25px;
        border: 1px solid rgba(245, 240, 235, 0.2);
        border-radius: 50px;
        background: rgba(255, 255, 255, 0.1);
        color: #f5f0eb;
        font-size: 0.95rem;
        outline: none;
        transition: all 0.3s ease;
    }

    .cta-input::placeholder {
        color: rgba(245, 240, 235, 0.5);
    }

    .cta-input:focus {
        background: rgba(255, 255, 255, 0.15);
        border-color: rgba(245, 240, 235, 0.4);
    }

    .cta-btn {
        padding: 16px 35px;
        background: #f5f0eb;
        color: #5c3a1e;
        border: none;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        letter-spacing: 2px;
    }

    .cta-btn:hover {
        background: #fff;
        transform: scale(1.05);
    }

    /* Footer */
    .footer {
        background: #2a1810;
        padding: 80px 5% 40px;
        color: rgba(245, 240, 235, 0.7);
    }

    .footer-grid {
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 60px;
        margin-bottom: 60px;
    }

    .footer-brand h3 {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        color: #f5f0eb;
        margin-bottom: 20px;
        letter-spacing: 3px;
    }

    .footer-brand p {
        font-size: 0.9rem;
        line-height: 1.9;
        margin-bottom: 25px;
    }

    .footer-social {
        display: flex;
        gap: 15px;
    }

    .social-icon {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: rgba(245, 240, 235, 0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #f5f0eb;
        text-decoration: none;
        transition: all 0.3s ease;
        font-size: 1rem;
    }

    .social-icon:hover {
        background: #8b5a2b;
        transform: translateY(-3px);
    }

    .footer-col h4 {
        font-family: 'Noto Serif SC', serif;
        font-size: 1rem;
        color: #f5f0eb;
        margin-bottom: 25px;
        letter-spacing: 2px;
    }

    .footer-col ul {
        list-style: none;
    }

    .footer-col ul li {
        margin-bottom: 12px;
    }

    .footer-col ul li a {
        color: rgba(245, 240, 235, 0.6);
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s ease;
    }

    .footer-col ul li a:hover {
        color: #c4a882;
    }

    .footer-bottom {
        max-width: 1400px;
        margin: 0 auto;
        padding-top: 30px;
        border-top: 1px solid rgba(245, 240, 235, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.8rem;
        color: rgba(245, 240, 235, 0.4);
    }

    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }

    /* Responsive */
    @media (max-width: 1024px) {
        .hero-content {
            grid-template-columns: 1fr;
            text-align: center;
        }
        .hero-desc {
            margin: 0 auto 40px;
        }
        .hero-visual {
            height: 400px;
        }
        .story-grid {
            grid-template-columns: 1fr;
        }
        .products-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        .features-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        .gallery-grid {
            grid-template-columns: repeat(2, 1fr);
            grid-template-rows: repeat(3, 200px);
        }
        .gallery-item.large {
            grid-column: span 2;
            grid-row: span 1;
        }
        .testimonials-grid {
            grid-template-columns: 1fr;
        }
        .footer-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 768px) {
        .nav-links {
            display: none;
        }
        .hero-title {
            font-size: 2.2rem;
        }
        .products-grid {
            grid-template-columns: 1fr;
        }
        .features-grid {
            grid-template-columns: 1fr;
        }
        .gallery-grid {
            grid-template-columns: 1fr;
            grid-template-rows: repeat(6, 200px);
        }
        .gallery-item.large,
        .gallery-item.wide {
            grid-column: span 1;
        }
        .footer-grid {
            grid-template-columns: 1fr;
        }
        .cta-form {
            flex-direction: column;
        }
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f5f0eb;
    }
    ::-webkit-scrollbar-thumb {
        background: #c4a882;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #a08060;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="nav-container">
    <div class="nav-inner">
        <a href="#" class="nav-logo">
            洋语楼
            <span>YANGYULOU COFFEE</span>
        </a>
        <ul class="nav-links">
            <li><a href="#home">首页</a></li>
            <li><a href="#story">品牌故事</a></li>
            <li><a href="#products">精选咖啡</a></li>
            <li><a href="#gallery">咖啡美学</a></li>
            <li><a href="#contact">联系我们</a></li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section" id="home">
    <div class="hero-bg-pattern"></div>
    <div class="hero-content">
        <div class="hero-text">
            <div class="hero-subtitle">Artisan Coffee Since 2018</div>
            <h1 class="hero-title">
                在洋语楼<br>
                品味<span class="highlight">时光</span>的醇香
            </h1>
            <p class="hero-desc">
                每一颗咖啡豆都承载着远方的风土与阳光，每一杯咖啡都是一场与自然的对话。
                洋语楼，用匠心守护咖啡本真的味道。
            </p>
            <div>
                <a href="#products" class="hero-btn">探索咖啡</a>
                <a href="#story" class="hero-btn-secondary">品牌故事</a>
            </div>
        </div>
        <div class="hero-visual">
            <img src="https://images.unsplash.com/photo-1497935586351-b67a49e012bf?w=800&q=80" class="hero-image-main" alt="Coffee Art">
            <div class="hero-float-card float-card-1">
                <div class="float-card-icon">☕</div>
                <div class="float-card-text">精选阿拉比卡</div>
                <div class="float-card-sub">埃塞俄比亚 · 耶加雪菲</div>
            </div>
            <div class="hero-float-card float-card-2">
                <div class="float-card-icon">🌸</div>
                <div class="float-card-text">花香风味</div>
                <div class="float-card-sub">茉莉 · 柑橘 · 蜂蜜</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Story Section
st.markdown("""
<div class="section" id="story">
    <div class="section-header">
        <div class="section-label">Our Story</div>
        <h2 class="section-title">品牌故事</h2>
        <p class="section-desc">从一颗种子到一杯醇香，洋语楼始终追寻咖啡最纯粹的美好</p>
    </div>
    <div class="story-grid">
        <div class="story-image">
            <img src="https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=800&q=80" alt="Coffee Story">
        </div>
        <div class="story-content">
            <h3>源于热爱，成于匠心</h3>
            <p>
                洋语楼创立于2018年，名字取自"洋"——来自远方的咖啡豆，"语"——每一杯咖啡都在诉说故事，"楼"——一方静谧的品味空间。
            </p>
            <p>
                我们深入埃塞俄比亚、哥伦比亚、危地马拉等全球优质咖啡产区，与当地农户建立直接贸易关系，确保每一颗咖啡豆都来自可持续种植的优质庄园。
            </p>
            <p>
                从选豆、烘焙到萃取，每一个环节都由资深咖啡师精心把控。我们相信，好的咖啡不仅是饮品，更是一种生活态度。
            </p>
            <div class="story-stats">
                <div class="stat-item">
                    <h4>6+</h4>
                    <p>年匠心传承</p>
                </div>
                <div class="stat-item">
                    <h4>12</h4>
                    <p>全球产区合作</p>
                </div>
                <div class="stat-item">
                    <h4>50K+</h4>
                    <p>满意顾客</p>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
<div class="section" style="background: linear-gradient(180deg, #ede6de 0%, #f5f0eb 100%);">
    <div class="section-header">
        <div class="section-label">Why Choose Us</div>
        <h2 class="section-title">我们的承诺</h2>
        <p class="section-desc">每一个细节，都是对品质的执着追求</p>
    </div>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">🌱</div>
            <h4 class="feature-title">源头直采</h4>
            <p class="feature-desc">直接与全球优质产区农户合作，确保每一颗咖啡豆的可追溯性与新鲜度</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔥</div>
            <h4 class="feature-title">小批量烘焙</h4>
            <p class="feature-desc">采用德国进口烘焙设备，小批量精准控温，释放咖啡豆最佳风味</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🌸</div>
            <h4 class="feature-title">花香风味</h4>
            <p class="feature-desc">精选花香型咖啡豆，让每一口都充满茉莉、柑橘与蜂蜜的优雅层次</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">♻️</div>
            <h4 class="feature-title">可持续理念</h4>
            <p class="feature-desc">支持公平贸易与环保包装，让每一次品尝都成为对地球的温柔呵护</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Products Section
st.markdown("""
<div class="section products-section" id="products">
    <div class="section-header">
        <div class="section-label">Our Collection</div>
        <h2 class="section-title">精选咖啡</h2>
        <p class="section-desc">从世界各地甄选而来的优质咖啡豆，每一款都有独特的风味故事</p>
    </div>
    <div class="products-grid">
        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=600&q=80" class="product-image" alt="耶加雪菲">
            <span class="product-badge">人气推荐</span>
            <div class="product-info">
                <div class="product-category">Single Origin</div>
                <h3 class="product-name">埃塞俄比亚 · 耶加雪菲</h3>
                <p class="product-desc">花香馥郁，带有茉莉、柠檬与蜂蜜的清新风味，酸度明亮，余韵悠长。</p>
                <div class="product-footer">
                    <div class="product-price">¥128 <span>¥158</span></div>
                    <button class="add-cart-btn">加入购物车</button>
                </div>
            </div>
        </div>
        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&q=80" class="product-image" alt="哥伦比亚瑰夏">
            <span class="product-badge">限量臻品</span>
            <div class="product-info">
                <div class="product-category">Limited Edition</div>
                <h3 class="product-name">哥伦比亚 · 瑰夏</h3>
                <p class="product-desc">稀有品种，带有热带水果、玫瑰花瓣与焦糖的复杂层次，口感丝滑细腻。</p>
                <div class="product-footer">
                    <div class="product-price">¥268 <span>¥328</span></div>
                    <button class="add-cart-btn">加入购物车</button>
                </div>
            </div>
        </div>
        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1504630083234-14187a9df0f5?w=600&q=80" class="product-image" alt="危地马拉安提瓜">
            <div class="product-info">
                <div class="product-category">Single Origin</div>
                <h3 class="product-name">危地马拉 · 安提瓜</h3>
                <p class="product-desc">火山土壤孕育的醇厚风味，带有可可、坚果与烟熏的深邃口感。</p>
                <div class="product-footer">
                    <div class="product-price">¥98 <span>¥128</span></div>
                    <button class="add-cart-btn">加入购物车</button>
                </div>
            </div>
        </div>
        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1611854779393-1b2da9d400fe?w=600&q=80" class="product-image" alt="肯尼亚AA">
            <span class="product-badge">新品尝鲜</span>
            <div class="product-info">
                <div class="product-category">New Arrival</div>
                <h3 class="product-name">肯尼亚 · AA级</h3>
                <p class="product-desc">黑醋栗与红酒般的果酸，搭配黑巧克力的浓郁尾韵，层次丰富。</p>
                <div class="product-footer">
                    <div class="product-price">¥148 <span>¥178</span></div>
                    <button class="add-cart-btn">加入购物车</button>
                </div>
            </div>
        </div>
        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1587734195503-904fca47e0e9?w=600&q=80" class="product-image" alt="巴西喜拉多">
            <div class="product-info">
                <div class="product-category">Single Origin</div>
                <h3 class="product-name">巴西 · 喜拉多</h3>
                <p class="product-desc">经典的坚果与巧克力风味，低酸醇厚，适合日常享用的平衡之选。</p>
                <div class="product-footer">
                    <div class="product-price">¥88 <span>¥108</span></div>
                    <button class="add-cart-btn">加入购物车</button>
                </div>
            </div>
        </div>
        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&q=80" class="product-image" alt="洋语楼特调">
            <span class="product-badge">招牌特调</span>
            <div class="product-info">
                <div class="product-category">House Blend</div>
                <h3 class="product-name">洋语楼 · 花语特调</h3>
                <p class="product-desc">独家拼配配方，融合花香与果香，口感圆润饱满，是洋语楼的招牌之作。</p>
                <div class="product-footer">
                    <div class="product-price">¥118 <span>¥138</span></div>
                    <button class="add-cart-btn">加入购物车</button>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Gallery Section
st.markdown("""
<div class="section" id="gallery">
    <div class="section-header">
        <div class="section-label">Coffee Aesthetics</div>
        <h2 class="section-title">咖啡美学</h2>
        <p class="section-desc">咖啡与花的艺术交融，每一帧都是生活的诗意</p>
    </div>
    <div class="gallery-grid">
        <div class="gallery-item large">
            <img src="https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=800&q=80" alt="Coffee Beans">
            <div class="gallery-overlay">
                <h4>精选咖啡豆</h4>
                <p>每一颗都是自然的馈赠</p>
            </div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1511920170033-f8396924c348?w=600&q=80" alt="Latte Art">
            <div class="gallery-overlay">
                <h4>拉花艺术</h4>
                <p>指尖上的咖啡画卷</p>
            </div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=600&q=80" alt="Coffee Shop">
            <div class="gallery-overlay">
                <h4>静谧空间</h4>
                <p>城市中的咖啡绿洲</p>
            </div>
        </div>
        <div class="gallery-item wide">
            <img src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800&q=80" alt="Flower Coffee">
            <div class="gallery-overlay">
                <h4>花与咖啡</h4>
                <p>自然与醇香的完美邂逅</p>
            </div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=600&q=80" alt="Pour Over">
            <div class="gallery-overlay">
                <h4>手冲时光</h4>
                <p>慢下来的仪式感</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonials Section
st.markdown("""
<div class="section" style="background: linear-gradient(180deg, #f5f0eb 0%, #ede6de 100%);">
    <div class="section-header">
        <div class="section-label">Testimonials</div>
        <h2 class="section-title">顾客心声</h2>
        <p class="section-desc">听听咖啡爱好者们怎么说</p>
    </div>
    <div class="testimonials-grid">
        <div class="testimonial-card">
            <div class="stars">★★★★★</div>
            <p class="testimonial-text">
                洋语楼的耶加雪菲是我喝过最惊艳的单品咖啡，花香层次丰富，每一口都像在品尝春天的味道。包装也很精美，送礼自用两相宜。
            </p>
            <div class="testimonial-author">
                <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&q=80" class="author-avatar" alt="User">
                <div class="author-info">
                    <h5>林小雅</h5>
                    <p>咖啡爱好者 · 上海</p>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <div class="stars">★★★★★</div>
            <p class="testimonial-text">
                作为一个每天离不开咖啡的人，洋语楼的花语特调已经成为我的日常必备。口感圆润，花香与果香的平衡恰到好处，性价比也很高。
            </p>
            <div class="testimonial-author">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&q=80" class="author-avatar" alt="User">
                <div class="author-info">
                    <h5>陈明远</h5>
                    <p>设计师 · 北京</p>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <div class="stars">★★★★★</div>
            <p class="testimonial-text">
                第一次尝试哥伦比亚瑰夏就被征服了，热带水果的风味非常突出，玫瑰香气若隐若现。洋语楼的品质确实值得信赖，已经回购多次。
            </p>
            <div class="testimonial-author">
                <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&q=80" class="author-avatar" alt="User">
                <div class="author-info">
                    <h5>王思琪</h5>
                    <p>美食博主 · 杭州</p>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-section" id="contact">
    <div class="cta-content">
        <h2 class="cta-title">开启您的咖啡之旅</h2>
        <p class="cta-desc">
            订阅洋语楼 newsletter，第一时间获取新品资讯、咖啡知识分享与专属优惠。
            让每一杯咖啡，都成为生活中的小确幸。
        </p>
        <div class="cta-form">
            <input type="email" class="cta-input" placeholder="请输入您的邮箱地址">
            <button class="cta-btn">立即订阅</button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div class="footer-grid">
        <div class="footer-brand">
            <h3>洋语楼</h3>
            <p>
                洋语楼咖啡，致力于将世界各地最优质的咖啡豆带给每一位爱好者。
                我们相信，一杯好咖啡，能让生活更有温度。
            </p>
            <div class="footer-social">
                <a href="#" class="social-icon">📷</a>
                <a href="#" class="social-icon">🐦</a>
                <a href="#" class="social-icon">📱</a>
                <a href="#" class="social-icon">📺</a>
            </div>
        </div>
        <div class="footer-col">
            <h4>产品系列</h4>
            <ul>
                <li><a href="#">单品咖啡</a></li>
                <li><a href="#">拼配咖啡</a></li>
                <li><a href="#">限量臻品</a></li>
                <li><a href="#">咖啡器具</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>关于我们</h4>
            <ul>
                <li><a href="#">品牌故事</a></li>
                <li><a href="#">咖啡产地</a></li>
                <li><a href="#">烘焙工艺</a></li>
                <li><a href="#">可持续发展</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>客户服务</h4>
            <ul>
                <li><a href="#">配送说明</a></li>
                <li><a href="#">退换政策</a></li>
                <li><a href="#">常见问题</a></li>
                <li><a href="#">联系我们</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <span>© 2024 洋语楼咖啡 YangYuLou Coffee. All rights reserved.</span>
        <span>用心烘焙 · 品味生活</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Smooth scroll JavaScript
st.markdown("""
<script>
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        const nav = document.querySelector('.nav-container');
        if (window.scrollY > 50) {
            nav.style.boxShadow = '0 2px 20px rgba(92, 58, 30, 0.1)';
        } else {
            nav.style.boxShadow = 'none';
        }
    });
</script>
""", unsafe_allow_html=True)
