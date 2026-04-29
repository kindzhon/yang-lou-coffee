<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>洋语楼咖啡 | 艺术咖啡品牌</title>
    <style>
        :root {
            --cream: #FAF7F2;
            --warm-cream: #F5EDE3;
            --soft-blush: #F0DFD4;
            --rose: #E8C4B8;
            --dusty-rose: #D4A99A;
            --gold: #C4A882;
            --warm-gold: #B8946A;
            --coffee-brown: #8B5E3C;
            --deep-coffee: #5C3A21;
            --dark-coffee: #3C2415;
            --soft-white: #FFFBF6;
            --card-bg: #FFFDF9;
            --text-dark: #2C1810;
            --text-medium: #5C3A21;
            --text-light: #8B6B5A;
            --border-soft: #E8D5C4;
            --shadow-soft: 0 4px 20px rgba(60, 36, 21, 0.06);
            --shadow-medium: 0 8px 32px rgba(60, 36, 21, 0.1);
            --shadow-hover: 0 14px 40px rgba(60, 36, 21, 0.16);
            --radius-sm: 10px;
            --radius-md: 16px;
            --radius-lg: 24px;
            --radius-xl: 32px;
            --transition-smooth: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', 'Noto Serif SC', 'STSong', 'Songti SC', 'SimSun', 'KaiTi', serif;
            background-color: var(--cream);
            color: var(--text-dark);
            line-height: 1.7;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        /* ============ 花瓣飘落动画 ============ */
        .petal-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        }

        .petal {
            position: absolute;
            top: -60px;
            opacity: 0;
            animation: petalFall linear infinite;
            pointer-events: none;
        }

        .petal::before {
            content: '';
            display: block;
            width: 100%;
            height: 100%;
            border-radius: 50% 0 50% 50%;
            background: var(--rose);
            opacity: 0.55;
            transform: rotate(45deg);
        }

        .petal:nth-child(1) {
            left: 5%;
            width: 22px;
            height: 22px;
            animation-duration: 14s;
            animation-delay: 0s;
        }
        .petal:nth-child(2) {
            left: 15%;
            width: 16px;
            height: 16px;
            animation-duration: 18s;
            animation-delay: 2s;
        }
        .petal:nth-child(3) {
            left: 25%;
            width: 20px;
            height: 20px;
            animation-duration: 16s;
            animation-delay: 4s;
        }
        .petal:nth-child(4) {
            left: 38%;
            width: 14px;
            height: 14px;
            animation-duration: 20s;
            animation-delay: 1s;
        }
        .petal:nth-child(5) {
            left: 50%;
            width: 24px;
            height: 24px;
            animation-duration: 15s;
            animation-delay: 5s;
        }
        .petal:nth-child(6) {
            left: 62%;
            width: 18px;
            height: 18px;
            animation-duration: 17s;
            animation-delay: 3s;
        }
        .petal:nth-child(7) {
            left: 75%;
            width: 21px;
            height: 21px;
            animation-duration: 19s;
            animation-delay: 6s;
        }
        .petal:nth-child(8) {
            left: 85%;
            width: 15px;
            height: 15px;
            animation-duration: 13s;
            animation-delay: 1.5s;
        }
        .petal:nth-child(9) {
            left: 92%;
            width: 19px;
            height: 19px;
            animation-duration: 16.5s;
            animation-delay: 3.5s;
        }
        .petal:nth-child(10) {
            left: 10%;
            width: 17px;
            height: 17px;
            animation-duration: 21s;
            animation-delay: 7s;
        }
        .petal:nth-child(11) {
            left: 45%;
            width: 23px;
            height: 23px;
            animation-duration: 18.5s;
            animation-delay: 8s;
        }
        .petal:nth-child(12) {
            left: 70%;
            width: 13px;
            height: 13px;
            animation-duration: 22s;
            animation-delay: 2.5s;
        }

        @keyframes petalFall {
            0% {
                transform: translateY(-60px) rotate(0deg) translateX(0px);
                opacity: 0;
            }
            5% {
                opacity: 0.55;
            }
            30% {
                transform: translateY(30vh) rotate(120deg) translateX(40px);
                opacity: 0.5;
            }
            60% {
                transform: translateY(60vh) rotate(260deg) translateX(-30px);
                opacity: 0.4;
            }
            90% {
                transform: translateY(90vh) rotate(340deg) translateX(20px);
                opacity: 0.1;
            }
            100% {
                transform: translateY(105vh) rotate(400deg) translateX(-10px);
                opacity: 0;
            }
        }

        /* ============ 导航栏 ============ */
        .navbar {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(250, 247, 242, 0.88);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-soft);
            padding: 0 2rem;
            transition: var(--transition-smooth);
        }

        .navbar-inner {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 68px;
        }

        .nav-logo {
            font-size: 1.6rem;
            font-weight: bold;
            color: var(--deep-coffee);
            letter-spacing: 0.04em;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: var(--transition-smooth);
            cursor: pointer;
        }

        .nav-logo:hover {
            color: var(--coffee-brown);
        }

        .nav-logo .logo-icon {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: linear-gradient(135deg, #8B5E3C, #5C3A21);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            color: #FFFBF6;
            box-shadow: 0 2px 10px rgba(92, 58, 33, 0.25);
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 0.5rem;
            align-items: center;
        }

        .nav-links li a {
            text-decoration: none;
            color: var(--text-medium);
            padding: 0.6rem 1.2rem;
            border-radius: 25px;
            font-size: 0.95rem;
            letter-spacing: 0.03em;
            transition: var(--transition-smooth);
            cursor: pointer;
            position: relative;
            font-weight: 500;
        }

        .nav-links li a:hover,
        .nav-links li a.active {
            color: var(--deep-coffee);
            background: rgba(196, 168, 130, 0.2);
        }

        .nav-links li a.active::after {
            content: '';
            position: absolute;
            bottom: 4px;
            left: 50%;
            transform: translateX(-50%);
            width: 18px;
            height: 3px;
            background: var(--coffee-brown);
            border-radius: 3px;
        }

        .nav-cart-btn {
            background: var(--coffee-brown);
            color: #FFFBF6 !important;
            padding: 0.6rem 1.4rem !important;
            border-radius: 25px !important;
            font-weight: 600 !important;
            letter-spacing: 0.04em;
            box-shadow: 0 2px 12px rgba(139, 94, 60, 0.3);
            transition: var(--transition-smooth) !important;
            cursor: pointer;
            border: none;
        }

        .nav-cart-btn:hover {
            background: var(--deep-coffee) !important;
            box-shadow: 0 4px 20px rgba(92, 58, 33, 0.4) !important;
            transform: translateY(-1px);
            color: #FFFBF6 !important;
        }

        /* 移动端菜单按钮 */
        .nav-mobile-toggle {
            display: none;
            background: none;
            border: none;
            font-size: 1.8rem;
            cursor: pointer;
            color: var(--deep-coffee);
            padding: 0.4rem;
        }

        /* ============ 主视觉区 Hero ============ */
        .hero-section {
            position: relative;
            max-width: 1200px;
            margin: 2rem auto;
            padding: 3.5rem 2.5rem;
            background: linear-gradient(160deg, #FFFBF6 0%, #F5EDE3 30%, #F0DFD4 60%, #FDF5F0 100%);
            border-radius: var(--radius-xl);
            text-align: center;
            box-shadow: var(--shadow-soft);
            overflow: hidden;
            z-index: 1;
        }

        .hero-section::before {
            content: '';
            position: absolute;
            top: -80px;
            right: -60px;
            width: 280px;
            height: 280px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(232, 196, 184, 0.35) 0%, transparent 70%);
            pointer-events: none;
            z-index: 0;
        }

        .hero-section::after {
            content: '';
            position: absolute;
            bottom: -60px;
            left: -40px;
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(196, 168, 130, 0.3) 0%, transparent 70%);
            pointer-events: none;
            z-index: 0;
        }

        .hero-content {
            position: relative;
            z-index: 1;
        }

        .hero-badge {
            display: inline-block;
            background: rgba(196, 168, 130, 0.2);
            color: var(--coffee-brown);
            padding: 0.5rem 1.4rem;
            border-radius: 30px;
            font-size: 0.9rem;
            letter-spacing: 0.06em;
            margin-bottom: 1.5rem;
            font-weight: 500;
            border: 1px solid rgba(196, 168, 130, 0.35);
        }

        .hero-title {
            font-size: clamp(2.4rem, 5vw, 3.8rem);
            font-weight: bold;
            color: var(--dark-coffee);
            letter-spacing: 0.05em;
            margin-bottom: 0.8rem;
            line-height: 1.25;
        }

        .hero-title .accent {
            color: var(--coffee-brown);
            position: relative;
        }

        .hero-title .flower-dot {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: var(--rose);
            border-radius: 50%;
            margin: 0 4px;
            vertical-align: middle;
            animation: dotPulse 2s ease-in-out infinite;
        }

        @keyframes dotPulse {
            0%,
            100% {
                transform: scale(1);
                opacity: 0.7;
            }
            50% {
                transform: scale(1.8);
                opacity: 1;
            }
        }

        .hero-subtitle {
            font-size: 1.2rem;
            color: var(--text-light);
            letter-spacing: 0.05em;
            margin-bottom: 2rem;
            font-weight: 400;
            max-width: 560px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero-cta {
            display: inline-flex;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
        }

        .btn-primary {
            background: var(--coffee-brown);
            color: #FFFBF6;
            padding: 0.85rem 2.2rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            letter-spacing: 0.05em;
            font-size: 1rem;
            transition: var(--transition-smooth);
            box-shadow: 0 4px 16px rgba(139, 94, 60, 0.3);
            cursor: pointer;
            border: none;
            display: inline-block;
        }

        .btn-primary:hover {
            background: var(--deep-coffee);
            box-shadow: 0 8px 28px rgba(92, 58, 33, 0.4);
            transform: translateY(-2px);
        }

        .btn-outline {
            background: transparent;
            color: var(--coffee-brown);
            padding: 0.85rem 2.2rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            letter-spacing: 0.05em;
            font-size: 1rem;
            transition: var(--transition-smooth);
            border: 2px solid var(--coffee-brown);
            cursor: pointer;
            display: inline-block;
        }

        .btn-outline:hover {
            background: rgba(139, 94, 60, 0.08);
            transform: translateY(-2px);
        }

        /* 咖啡豆装饰 */
        .coffee-bean-decor {
            position: absolute;
            pointer-events: none;
            z-index: 0;
            opacity: 0.2;
            font-size: 3rem;
        }
        .coffee-bean-decor.b1 {
            top: 15%;
            left: 8%;
            transform: rotate(-25deg);
            font-size: 2.8rem;
        }
        .coffee-bean-decor.b2 {
            bottom: 20%;
            right: 6%;
            transform: rotate(30deg);
            font-size: 3.5rem;
            opacity: 0.16;
        }
        .coffee-bean-decor.b3 {
            top: 40%;
            right: 12%;
            transform: rotate(50deg);
            font-size: 2.2rem;
            opacity: 0.22;
        }

        /* ============ 通用区块 ============ */
        .section-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 2rem 3rem;
            position: relative;
            z-index: 1;
        }

        .section-header {
            text-align: center;
            margin-bottom: 2.5rem;
        }

        .section-label {
            display: inline-block;
            color: var(--coffee-brown);
            font-size: 0.9rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.6rem;
            font-weight: 500;
        }

        .section-title {
            font-size: clamp(1.8rem, 3.5vw, 2.5rem);
            color: var(--dark-coffee);
            letter-spacing: 0.04em;
            margin-bottom: 0.5rem;
        }

        .section-divider {
            width: 50px;
            height: 3px;
            background: var(--gold);
            margin: 0.8rem auto;
            border-radius: 3px;
        }

        /* ============ 商品卡片网格 ============ */
        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.8rem;
        }

        .product-card {
            background: var(--card-bg);
            border-radius: var(--radius-lg);
            padding: 1.8rem;
            box-shadow: var(--shadow-soft);
            transition: var(--transition-smooth);
            border: 1px solid transparent;
            position: relative;
            overflow: hidden;
            cursor: pointer;
            text-align: center;
        }

        .product-card:hover {
            box-shadow: var(--shadow-hover);
            transform: translateY(-4px);
            border-color: var(--border-soft);
        }

        .product-card .product-icon-wrapper {
            width: 80px;
            height: 80px;
            margin: 0 auto 1.2rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.4rem;
            transition: var(--transition-smooth);
        }

        .product-card:nth-child(1) .product-icon-wrapper {
            background: linear-gradient(135deg, #F5EDE3, #E8D5C4);
        }
        .product-card:nth-child(2) .product-icon-wrapper {
            background: linear-gradient(135deg, #F0DFD4, #E8C4B8);
        }
        .product-card:nth-child(3) .product-icon-wrapper {
            background: linear-gradient(135deg, #E8D5C4, #D4B896);
        }
        .product-card:nth-child(4) .product-icon-wrapper {
            background: linear-gradient(135deg, #F5EDE3, #F0DFD4);
        }
        .product-card:nth-child(5) .product-icon-wrapper {
            background: linear-gradient(135deg, #FFF5EE, #F0DFD4);
        }
        .product-card:nth-child(6) .product-icon-wrapper {
            background: linear-gradient(135deg, #FAF0E6, #E8D5C4);
        }

        .product-card h3 {
            font-size: 1.25rem;
            color: var(--deep-coffee);
            margin-bottom: 0.5rem;
            letter-spacing: 0.03em;
        }

        .product-card .product-desc {
            font-size: 0.9rem;
            color: var(--text-light);
            margin-bottom: 1rem;
            line-height: 1.5;
            min-height: 44px;
        }

        .product-card .product-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            justify-content: center;
            margin-bottom: 1rem;
        }

        .product-card .tag {
            font-size: 0.75rem;
            padding: 0.25rem 0.7rem;
            border-radius: 15px;
            background: rgba(196, 168, 130, 0.18);
            color: var(--coffee-brown);
            letter-spacing: 0.03em;
        }

        .product-card .price {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--coffee-brown);
            margin-bottom: 1.2rem;
            letter-spacing: 0.03em;
        }

        .product-card .price .unit {
            font-size: 0.85rem;
            font-weight: 400;
            color: var(--text-light);
        }

        .btn-add-cart {
            background: var(--coffee-brown);
            color: #FFFBF6;
            border: none;
            padding: 0.65rem 1.6rem;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 600;
            letter-spacing: 0.04em;
            font-size: 0.9rem;
            transition: var(--transition-smooth);
            box-shadow: 0 2px 10px rgba(139, 94, 60, 0.25);
            width: 100%;
            font-family: inherit;
        }

        .btn-add-cart:hover {
            background: var(--deep-coffee);
            box-shadow: 0 6px 20px rgba(92, 58, 33, 0.35);
            transform: translateY(-1px);
        }

        .btn-add-cart.added {
            background: #5a8a5a;
            box-shadow: 0 2px 10px rgba(90, 138, 90, 0.3);
        }

        /* ============ 购物车侧边栏样式 ============ */
        .cart-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.8rem 0;
            border-bottom: 1px solid var(--border-soft);
        }
        .cart-item-name {
            font-weight: 500;
            color: var(--text-dark);
        }
        .cart-item-price {
            color: var(--coffee-brown);
            font-weight: 600;
        }
        .cart-total {
            font-size: 1.2rem;
            font-weight: bold;
            color: var(--deep-coffee);
            text-align: right;
            padding: 1rem 0;
            border-top: 2px solid var(--gold);
            margin-top: 0.5rem;
        }

        /* ============ 品牌故事区 ============ */
        .about-section {
            background: linear-gradient(180deg, #FFFBF6 0%, #FDF5F0 50%, #FFFBF6 100%);
            border-radius: var(--radius-xl);
            padding: 3rem 2.5rem;
            text-align: center;
            box-shadow: var(--shadow-soft);
            position: relative;
            overflow: hidden;
        }

        .about-section::before {
            content: '';
            position: absolute;
            top: -50px;
            left: 50%;
            transform: translateX(-50%);
            width: 300px;
            height: 300px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(232, 196, 184, 0.2) 0%, transparent 70%);
            pointer-events: none;
        }

        .about-text {
            max-width: 650px;
            margin: 0 auto;
            font-size: 1.05rem;
            color: var(--text-medium);
            line-height: 1.9;
            position: relative;
            z-index: 1;
        }

        /* ============ 页脚 ============ */
        .footer {
            text-align: center;
            padding: 2.5rem;
            color: var(--text-light);
            font-size: 0.9rem;
            letter-spacing: 0.04em;
            border-top: 1px solid var(--border-soft);
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }

        .footer .footer-brand {
            font-size: 1.3rem;
            font-weight: bold;
            color: var(--deep-coffee);
            margin-bottom: 0.5rem;
            letter-spacing: 0.06em;
        }

        /* ============ Toast提示 ============ */
        .toast {
            position: fixed;
            top: 90px;
            right: 30px;
            z-index: 200;
            background: #5a8a5a;
            color: white;
            padding: 1rem 1.6rem;
            border-radius: 30px;
            font-weight: 600;
            letter-spacing: 0.04em;
            box-shadow: 0 8px 24px rgba(90, 138, 90, 0.4);
            animation: toastIn 0.4s ease-out, toastOut 0.4s ease-in 1.8s forwards;
            pointer-events: none;
            font-family: inherit;
        }

        @keyframes toastIn {
            from {
                transform: translateX(120%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        @keyframes toastOut {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(120%);
                opacity: 0;
            }
        }

        /* ============ 响应式 ============ */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
                position: absolute;
                top: 68px;
                left: 0;
                right: 0;
                background: rgba(250, 247, 242, 0.97);
                flex-direction: column;
                padding: 1rem;
                border-bottom: 1px solid var(--border-soft);
                box-shadow: var(--shadow-medium);
                gap: 0.3rem;
            }
            .nav-links.open {
                display: flex;
            }
            .nav-mobile-toggle {
                display: block;
            }
            .navbar-inner {
                height: 60px;
            }
            .hero-section {
                margin: 1rem;
                padding: 2.5rem 1.5rem;
                border-radius: var(--radius-lg);
            }
            .products-grid {
                grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
                gap: 1.2rem;
            }
            .section-container {
                padding: 1.5rem 1rem 2rem;
            }
            .about-section {
                padding: 2rem 1.5rem;
                border-radius: var(--radius-lg);
            }
            .hero-cta {
                flex-direction: column;
                align-items: center;
            }
            .toast {
                right: 15px;
                top: 75px;
                font-size: 0.85rem;
                padding: 0.8rem 1.2rem;
            }
        }

        @media (max-width: 480px) {
            .hero-title {
                font-size: 1.8rem;
            }
            .hero-subtitle {
                font-size: 0.95rem;
            }
            .products-grid {
                grid-template-columns: 1fr;
                gap: 1rem;
            }
            .product-card {
                padding: 1.4rem;
            }
        }

        /* 平滑滚动 */
        html {
            scroll-behavior: smooth;
        }
    </style>
</head>
<body>

    <!-- 花瓣飘落 -->
    <div class="petal-container">
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
    </div>

    <!-- Toast容器 -->
    <div id="toastContainer"></div>

    <!-- 导航栏 -->
    <nav class="navbar" id="navbar">
        <div class="navbar-inner">
            <a class="nav-logo" onclick="scrollToSection('hero')">
                <span class="logo-icon">☕</span>
                洋语楼咖啡
            </a>
            <button class="nav-mobile-toggle" id="mobileToggle" onclick="toggleMobileMenu()" aria-label="菜单">
                &#9776;
            </button>
            <ul class="nav-links" id="navLinks">
                <li><a class="active" onclick="scrollToSection('hero'); closeMobileMenu();">首页</a></li>
                <li><a onclick="scrollToSection('products'); closeMobileMenu();">精选商品</a></li>
                <li><a onclick="scrollToSection('about'); closeMobileMenu();">关于我们</a></li>
                <li><a class="nav-cart-btn" onclick="scrollToSection('cart-section'); closeMobileMenu();">
                        🛒 购物车 <span id="cartCountBadge">(0)</span>
                </a></li>
            </ul>
        </div>
    </nav>

    <!-- 主视觉区 -->
    <section class="hero-section" id="hero">
        <div class="coffee-bean-decor b1">🫘</div>
        <div class="coffee-bean-decor b2">🫘</div>
        <div class="coffee-bean-decor b3">🌿</div>
        <div class="hero-content">
            <span class="hero-badge">✦ 艺术咖啡品牌 ✦</span>
            <h1 class="hero-title">
                洋语楼<span class="flower-dot"></span>咖啡
            </h1>
            <p class="hero-subtitle">
                在咖啡豆与花瓣交织的香气里，<br>寻一段属于自己的静谧时光。
            </p>
            <div class="hero-cta">
                <button class="btn-primary" onclick="scrollToSection('products')">探索我们的咖啡</button>
                <button class="btn-outline" onclick="scrollToSection('about')">了解品牌故事</button>
            </div>
        </div>
    </section>

    <!-- 商品展示区 -->
    <div class="section-container" id="products">
        <div class="section-header">
            <span class="section-label">Our Selection</span>
            <h2 class="section-title">精选咖啡与好物</h2>
            <div class="section-divider"></div>
            <p style="color: var(--text-light); margin-top: 0.5rem;">每一款都承载着我们对品质的执着</p>
        </div>
        <div class="products-grid" id="productsGrid">
            <!-- 商品通过JS动态渲染 -->
        </div>
    </div>

    <!-- 购物车区 -->
    <div class="section-container" id="cart-section">
        <div class="section-header">
            <span class="section-label">Your Cart</span>
            <h2 class="section-title">🛒 您的购物车</h2>
            <div class="section-divider"></div>
        </div>
        <div style="max-width: 700px; margin: 0 auto; background: var(--card-bg); border-radius: var(--radius-lg); padding: 2rem; box-shadow: var(--shadow-soft);">
            <div id="cartItemsContainer">
                <p style="text-align:center; color: var(--text-light); padding: 2rem 0;">✨ 购物车是空的，去挑选心仪的咖啡吧~</p>
            </div>
            <div id="cartTotalContainer" style="display:none;"></div>
            <div id="checkoutForm" style="display:none; margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border-soft);">
                <h3 style="color: var(--deep-coffee); margin-bottom: 1rem; letter-spacing: 0.04em;">📝 填写订单信息</h3>
                <div style="display: flex; flex-direction: column; gap: 0.8rem;">
                    <input type="text" id="customerName" placeholder="您的姓名" style="padding: 0.7rem 1rem; border: 1.5px solid var(--border-soft); border-radius: 25px; font-family: inherit; font-size: 0.95rem; background: #FFFDF9; outline: none; transition: var(--transition-smooth);">
                    <input type="tel" id="customerPhone" placeholder="联系电话" style="padding: 0.7rem 1rem; border: 1.5px solid var(--border-soft); border-radius: 25px; font-family: inherit; font-size: 0.95rem; background: #FFFDF9; outline: none; transition: var(--transition-smooth);">
                    <textarea id="customerNote" placeholder="备注（选填）" rows="2" style="padding: 0.7rem 1rem; border: 1.5px solid var(--border-soft); border-radius: 18px; font-family: inherit; font-size: 0.95rem; background: #FFFDF9; outline: none; resize: vertical; transition: var(--transition-smooth);"></textarea>
                    <button class="btn-primary" onclick="submitOrder()" style="width:100%; font-family:inherit;">✨ 提交订单</button>
                </div>
            </div>
        </div>
    </div>

    <!-- 关于我们 -->
    <div class="section-container" id="about">
        <div class="about-section">
            <div class="section-header">
                <span class="section-label">About Us</span>
                <h2 class="section-title">洋语楼的故事</h2>
                <div class="section-divider"></div>
            </div>
            <div class="about-text">
                <p>
                    洋语楼咖啡，诞生于对咖啡艺术的热爱。<br>
                    我们相信，一杯好咖啡不仅仅是味蕾的享受，更是一场与自我的对话。
                </p>
                <p style="margin-top: 1rem;">
                    从哥伦比亚高原到埃塞俄比亚山谷，我们精心挑选每一颗咖啡豆，<br>
                    用匠心烘焙，以花香为伴，将自然的馈赠融入每一杯之中。
                </p>
                <p style="margin-top: 1rem;">
                    🌸 咖啡 · 豆香 · 花语 —— 这便是洋语楼。🌸
                </p>
            </div>
        </div>
    </div>

    <!-- 页脚 -->
    <div class="footer">
        <div class="footer-brand">☕ 洋语楼咖啡</div>
        <p>咖啡 · 豆香 · 花语 | 艺术咖啡品牌</p>
        <p style="margin-top: 0.4rem; font-size: 0.8rem;">&copy; 2024 洋语楼咖啡 YangYuLou Coffee. All rights reserved.</p>
    </div>

    <script>
        // ============ 商品数据 ============
        const products = [
            { id: 1, name: '洋语楼·经典手冲', icon: '☕', desc: '精选埃塞俄比亚耶加雪菲，手工慢冲，果酸明亮，回味甘甜。', tags: ['手冲', '果香', '经典'], price: 38,
                unit: '/杯' },
            { id: 2, name: '玫瑰拿铁', icon: '🌹', desc: '意式浓缩遇见玫瑰花瓣，丝滑奶泡中绽放花香，温柔了整个午后。', tags: ['拿铁', '花香',
                    '人气'], price: 42, unit: '/杯' },
            { id: 3, name: '哥伦比亚单品豆', icon: '🫘', desc: '哥伦比亚慧兰产区，中度烘焙，坚果与可可风味，回韵悠长。', tags: ['单品', '坚果', '精品'],
                price: 88, unit: '/袋(250g)' },
            { id: 4, name: '花语冷萃', icon: '🧊', desc: '12小时低温萃取，融入桂花与栀子花香，清爽中透着丝丝甜蜜。', tags: ['冷萃', '花香', '夏日'],
                price: 36, unit: '/瓶' },
            { id: 5, name: '桂花燕麦拿铁', icon: '🥛', desc: '植物基燕麦奶搭配桂花糖浆，乳糖不耐友好，秋日氛围感满分。', tags: ['植物基', '桂花',
                    '健康'], price: 40, unit: '/杯' },
            { id: 6, name: '精品挂耳礼盒', icon: '🎁', desc: '六款风味挂耳包，精美礼盒装，送礼自用皆是品味之选。', tags: ['礼盒', '挂耳', '送礼'],
                price: 128, unit: '/盒' },
        ];

        // ============ 购物车状态 ============
        let cart = [];

        function loadCart() {
            const saved = localStorage.getItem('yangyulou_cart');
            if (saved) {
                try { cart = JSON.parse(saved); } catch (e) { cart = []; }
            }
        }

        function saveCart() {
            localStorage.setItem('yangyulou_cart', JSON.stringify(cart));
            updateCartUI();
        }

        function addToCart(productId) {
            const product = products.find(p => p.id === productId);
            if (!product) return;
            const existing = cart.find(item => item.id === productId);
            if (existing) {
                existing.quantity += 1;
            } else {
                cart.push({
                    id: product.id,
                    name: product.name,
                    price: product.price,
                    unit: product.unit,
                    quantity: 1,
                    icon: product.icon,
                });
            }
            saveCart();
            showToast(`✅ 已添加：${product.name}`);
            // 按钮动画
            const btn = document.querySelector(`.btn-add-cart[data-id="${productId}"]`);
            if (btn) {
                btn.classList.add('added');
                btn.textContent = '✓ 已添加';
                setTimeout(() => {
                    btn.classList.remove('added');
                    btn.textContent = '加入购物车';
                }, 1500);
            }
        }

        function removeFromCart(index) {
            cart.splice(index, 1);
            saveCart();
            renderCart();
        }

        function updateQuantity(index, delta) {
            cart[index].quantity += delta;
            if (cart[index].quantity <= 0) {
                cart.splice(index, 1);
            }
            saveCart();
            renderCart();
        }

        function updateCartUI() {
            const countBadge = document.getElementById('cartCountBadge');
            if (countBadge) {
                const total = cart.reduce((sum, item) => sum + item.quantity, 0);
                countBadge.textContent = `(${total})`;
            }
        }

        function showToast(message) {
            const container = document.getElementById('toastContainer');
            const toast = document.createElement('div');
            toast.className = 'toast';
            toast.textContent = message;
            container.appendChild(toast);
            setTimeout(() => { toast.remove(); }, 2400);
        }

        // ============ 渲染商品卡片 ============
        function renderProducts() {
            const grid = document.getElementById('productsGrid');
            if (!grid) return;
            grid.innerHTML = products.map(p => `
                <div class="product-card">
                    <div class="product-icon-wrapper">${p.icon}</div>
                    <h3>${p.name}</h3>
                    <p class="product-desc">${p.desc}</p>
                    <div class="product-tags">
                        ${p.tags.map(t => `<span class="tag">${t}</span>`).join('')}
                    </div>
                    <div class="price">¥${p.price} <span class="unit">${p.unit}</span></div>
                    <button class="btn-add-cart" data-id="${p.id}" onclick="addToCart(${p.id})">加入购物车</button>
                </div>
            `).join('');
        }

        // ============ 渲染购物车 ============
        function renderCart() {
            const container = document.getElementById('cartItemsContainer');
            const totalContainer = document.getElementById('cartTotalContainer');
            const checkoutForm = document.getElementById('checkoutForm');
            if (!container) return;

            if (cart.length === 0) {
                container.innerHTML =
                    '<p style="text-align:center; color: var(--text-light); padding: 2rem 0;">✨ 购物车是空的，去挑选心仪的咖啡吧~</p>';
                if (totalContainer) totalContainer.style.display = 'none';
                if (checkoutForm) checkoutForm.style.display = 'none';
            } else {
                container.innerHTML = cart.map((item, index) => `
                    <div class="cart-item">
                        <div>
                            <span style="font-size:1.3rem; margin-right:0.5rem;">${item.icon}</span>
                            <span class="cart-item-name">${item.name}</span>
                            <span style="color:var(--text-light); font-size:0.85rem;">${item.unit}</span>
                        </div>
                        <div style="display:flex; align-items:center; gap:0.6rem;">
                            <button onclick="updateQuantity(${index}, -1)" style="background:var(--border-soft); border:none; width:28px; height:28px; border-radius:50%; cursor:pointer; font-size:1rem; color:var(--deep-coffee); font-weight:bold; line-height:1;">−</button>
                            <span style="font-weight:600; min-width:20px; text-align:center;">${item.quantity}</span>
                            <button onclick="updateQuantity(${index}, 1)" style="background:var(--border-soft); border:none; width:28px; height:28px; border-radius:50%; cursor:pointer; font-size:1rem; color:var(--deep-coffee); font-weight:bold; line-height:1;">+</button>
                            <span class="cart-item-price" style="margin-left:0.8rem;">¥${item.price * item.quantity}</span>
                            <button onclick="removeFromCart(${index})" style="background:none; border:none; cursor:pointer; font-size:1.1rem; color:#c0392b; padding:0 0.3rem;" title="删除">🗑</button>
                        </div>
                    </div>
                `).join('');

                const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
                if (totalContainer) {
                    totalContainer.style.display = 'block';
                    totalContainer.innerHTML = `<div class="cart-total">合计：¥${total}</div>`;
                }
                if (checkoutForm) {
                    checkoutForm.style.display = 'block';
                }
            }
            updateCartUI();
        }

        function submitOrder() {
            if (cart.length === 0) {
                showToast('⚠️ 购物车是空的，请先添加商品');
                return;
            }
            const name = document.getElementById('customerName')?.value.trim();
            const phone = document.getElementById('customerPhone')?.value.trim();
            if (!name || !phone) {
                showToast('⚠️ 请填写姓名和联系电话');
                return;
            }
            const note = document.getElementById('customerNote')?.value.trim() || '';
            const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
            const orderSummary = cart.map(item =>
                `${item.icon} ${item.name} ×${item.quantity} = ¥${item.price * item.quantity}`
            ).join('\n');

            // 模拟提交
            showToast('🎉 订单已提交！我们会尽快联系您～');

            // 打印订单信息到控制台（实际项目中发送到后端）
            console.log('=== 新订单 ===');
            console.log('客户:', name, phone);
            console.log('备注:', note);
            console.log('订单明细:\n', orderSummary);
            console.log('总计: ¥' + total);
            console.log('==============');

            // 清空购物车
            cart = [];
            saveCart();
            renderCart();
            if (document.getElementById('customerName')) document.getElementById('customerName').value = '';
            if (document.getElementById('customerPhone')) document.getElementById('customerPhone').value = '';
            if (document.getElementById('customerNote')) document.getElementById('customerNote').value = '';
            scrollToSection('cart-section');
        }

        // ============ 导航辅助 ============
        function scrollToSection(id) {
            const el = document.getElementById(id);
            if (el) {
                const offset = 80;
                const top = el.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({ top, behavior: 'smooth' });
            }
            // 更新导航active状态
            document.querySelectorAll('.nav-links li a').forEach(a => a.classList.remove('active'));
            const navLinks = document.querySelectorAll('.nav-links li a');
            navLinks.forEach(a => {
                if (a.textContent.includes(getNavLabel(id))) {
                    a.classList.add('active');
                }
            });
        }

        function getNavLabel(id) {
            const map = { 'hero': '首页', 'products': '精选商品', 'about': '关于我们', 'cart-section': '购物车' };
            return map[id] || '';
        }

        function toggleMobileMenu() {
            const links = document.getElementById('navLinks');
            if (links) links.classList.toggle('open');
        }

        function closeMobileMenu() {
            const links = document.getElementById('navLinks');
            if (links) links.classList.remove('open');
        }

        // ============ 滚动时更新导航高亮 ============
        function updateNavOnScroll() {
            const sections = ['hero', 'products', 'cart-section', 'about'];
            let current = 'hero';
            sections.forEach(id => {
                const el = document.getElementById(id);
                if (el) {
                    const rect = el.getBoundingClientRect();
                    if (rect.top <= 120) {
                        current = id;
                    }
                }
            });
            document.querySelectorAll('.nav-links li a').forEach(a => a.classList.remove('active'));
            const navLinks = document.querySelectorAll('.nav-links li a');
            navLinks.forEach(a => {
                if (a.textContent.includes(getNavLabel(current))) {
                    a.classList.add('active');
                }
            });
        }

        // ============ 初始化 ============
        function init() {
            loadCart();
            renderProducts();
            renderCart();
            updateCartUI();
            window.addEventListener('scroll', updateNavOnScroll);
            // 点击页面其他区域关闭移动菜单
            document.addEventListener('click', function(e) {
                const nav = document.getElementById('navLinks');
                const toggle = document.getElementById('mobileToggle');
                if (nav && nav.classList.contains('open') && !nav.contains(e.target) && e.target !== toggle && !toggle
                    .contains(e.target)) {
                    nav.classList.remove('open');
                }
            });
        }

        document.addEventListener('DOMContentLoaded', init);
    </script>
</body>
</html>
