import streamlit as st

# ---------------- 页面基础配置 ----------------
st.set_page_config(
    page_title="洋语楼咖啡 | Yangyulou Coffee",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- 全局样式注入 ----------------
st.markdown("""
<style>
  :root {
    --bg-cream: #f9f5f0;
    --text-dark: #3a3226;
    --accent-brown: #6b4c3b;
    --soft-pink: #e8d5c4;
    --btn-hover: #8c6b5d;
    --card-shadow: 0 6px 24px rgba(58,50,38,0.08);
  }
  body { font-family: 'Noto Serif SC', 'Songti SC', serif; background: var(--bg-cream); color: var(--text-dark); margin: 0; padding: 0; overflow-x: hidden; }
  [data-testid="stAppViewContainer"] { background: transparent !important; }
  [data-testid="stHeader"], [data-testid="stToolbar"] { display: none !important; }
  a { color: var(--accent-brown); text-decoration: none; transition: color 0.3s; }
  
  /* 导航栏 */
  .navbar { position: sticky; top: 0; z-index: 1000; background: rgba(255,255,255,0.85); backdrop-filter: blur(12px); padding: 1rem 3rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e0d5c9; }
  .brand { font-size: 1.4rem; font-weight: 600; letter-spacing: 1px; }
  .nav-links a { margin-left: 2.2rem; font-size: 0.95rem; }
  .nav-links a:hover { color: var(--accent-brown); }
  
  /* 主视觉 */
  .hero { position: relative; height: 80vh; background: url('https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat; display: flex; align-items: center; justify-content: center; text-align: center; color: white; }
  .hero::before { content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(58,50,38,0.55), rgba(107,76,59,0.35)); }
  .hero-content { position: relative; z-index: 2; max-width: 800px; padding: 0 2rem; }
  .hero h1 { font-size: 3rem; margin-bottom: 0.8rem; letter-spacing: 2px; line-height: 1.2; }
  .hero p { font-size: 1.15rem; margin-bottom: 2rem; opacity: 0.92; font-weight: 400; }
  .btn-primary { background: var(--accent-brown); color: white; padding: 0.85rem 2.4rem; border: none; border-radius: 50px; font-size: 1rem; cursor: pointer; transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1); box-shadow: 0 4px 15px rgba(107,76,59,0.25); display: inline-block; }
  .btn-primary:hover { background: var(--btn-hover); transform: translateY(-3px); box-shadow: 0 6px 20px rgba(107,76,59,0.35); }
  
  /* 商品网格 */
  .section { padding: 4.5rem 3rem; max-width: 1280px; margin: 0 auto; }
  .section-title { text-align: center; font-size: 2.4rem; margin-bottom: 3rem; color: var(--accent-brown); position: relative; }
  .section-title::after { content: '❀'; display: block; font-size: 1.4rem; margin-top: 0.6rem; opacity: 0.6; color: var(--soft-pink); }
  .product-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; }
  .product-card { background: #ffffff; border-radius: 18px; overflow: hidden; box-shadow: var(--card-shadow); transition: transform 0.4s ease, box-shadow 0.4s ease; cursor: pointer; position: relative; }
  .product-card:hover { transform: translateY(-8px); box-shadow: 0 12px 35px rgba(58,50,38,0.12); }
  .product-img { width: 100%; height: 230px; object-fit: cover; }
  .product-info { padding: 1.6rem; flex: 1; display: flex; flex-direction: column; }
  .product-name { font-size: 1.35rem; margin: 0 0 0.6rem; font-weight: 600; }
  .product-desc { color: #665c52; font-size: 0.92rem; line-height: 1.6; margin-bottom: auto; }
  .product-meta { display: flex; justify-content: space-between; align-items: center; margin-top: 1.2rem; padding-top: 1rem; border-top: 1px dashed #e8d5c4; }
  .product-price { font-size: 1.25rem; color: var(--accent-brown); font-weight: 600; }
  .btn-buy { background: transparent; border: 2px solid var(--accent-brown); color: var(--accent-brown); padding: 0.6rem 1.4rem; border-radius: 10px; cursor: pointer; font-weight: 500; transition: all 0.3s; }
  .btn-buy:hover { background: var(--accent-brown); color: white; }
  
  /* 购物车提示 */
  .cart-toast { position: fixed; bottom: 2rem; right: 2rem; background: var(--accent-brown); color: white; padding: 1rem 1.5rem; border-radius: 12px; box-shadow: 0 6px 20px rgba(0,0,0,0.2); opacity: 0; transform: translateY(20px); transition: all 0.4s; z-index: 2000; pointer-events: none; }
  .cart-toast.show { opacity: 1; transform: translateY(0); pointer-events: auto; }
  
  /* 页脚 */
  .footer { text-align: center; padding: 3rem 2rem; background: #f0e8df; margin-top: 2rem; color: #665c52; font-size: 0.85rem; border-top: 1px solid #e0d5c9; }
  @media (max-width: 768px) {
    .navbar { padding: 1rem 1.5rem; flex-direction: column; gap: 0.8rem; }
    .nav-links a { margin: 0 0.8rem; font-size: 0.85rem; }
    .hero h1 { font-size: 2.2rem; }
    .section { padding: 3rem 1.5rem; }
    .product-grid { grid-template-columns: 1fr; }
  }
</style>
""", unsafe_allow_html=True)

# ---------------- 导航栏 & 主视觉 ----------------
st.markdown("""
<div class="navbar">
  <div class="brand">洋语楼咖啡</div>
  <div class="nav-links">
    <a href="#hero">首页</a>
    <a href="#products">产品系列</a>
    <a href="#cart">购物车</a>
    <a href="#footer">联系我们</a>
  </div>
</div>
<div class="hero" id="hero">
  <div class="hero-content">
    <h1>时光慢煮，花香入咖</h1>
    <p>精选阿拉比卡豆，手工拼配自然花韵<br>每一口都是生活与艺术的温柔碰撞</p>
    <a href="#products" class="btn-primary">探索风味</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------- 商品展示区 ----------------
st.markdown('<h2 class="section-title" id="products">当季限定系列</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="product-grid">
  <div class="product-card" onclick="addToCart('玫瑰拿铁研磨粉', 89)">
    <img class="product-img" src="https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&w=600&q=80" alt="玫瑰拿铁">
    <div class="product-info">
      <h3 class="product-name">玫瑰拿铁研磨粉</h3>
      <p class="product-desc">大马士革玫瑰与耶加雪菲碰撞，清甜花香与柑橘果酸交织，适合手冲冷萃。</p>
      <div class="product-meta">
        <span class="product-price">¥89</span>
        <button class="btn-buy" onclick="event.stopPropagation(); addToCart('玫瑰拿铁研磨粉', 89)">加入购物车</button>
      </div>
    </div>
  </div>
  <div class="product-card" onclick="addToCart('茉莉冷萃浓缩液', 128)">
    <img class="product-img" src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=600&q=80" alt="茉莉冷萃">
    <div class="product-info">
      <h3 class="product-name">茉莉冷萃浓缩液</h3>
      <p class="product-desc">6小时低温萃取融入横县茉莉精华。开盖即饮，花香清透，夏日解暑首选。</p>
      <div class="product-meta">
        <span class="product-price">¥128</span>
        <button class="btn-buy" onclick="event.stopPropagation(); addToCart('茉莉冷萃浓缩液', 128)">加入购物车</button>
      </div>
    </div>
  </div>
  <div class="product-card" onclick="addToCart('豆蔻燕麦挂耳包', 76)">
    <img class="product-img" src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=600&q=80" alt="豆蔻燕麦">
    <div class="product-info">
      <h3 class="product-name">豆蔻燕麦挂耳包</h3>
      <p class="product-desc">中西香料哲学。肉豆蔻微辛与燕麦奶醇厚平衡，早餐唤醒利器。</p>
      <div class="product-meta">
        <span class="product-price">¥76</span>
        <button class="btn-buy" onclick="event.stopPropagation(); addToCart('豆蔻燕麦挂耳包', 76)">加入购物车</button>
      </div>
    </div>
  </div>
  <div class="product-card" onclick="addToCart('庭院日晒咖啡豆', 108)">
    <img class="product-img" src="https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=600&q=80" alt="日晒豆">
    <div class="product-info">
      <h3 class="product-name">庭院日晒咖啡豆</h3>
      <p class="product-desc">云南高山日晒豆，保留完整果壳发酵。风味：草莓果酱、太妃糖与干花香气。</p>
      <div class="product-meta">
        <span class="product-price">¥108</span>
        <button class="btn-buy" onclick="event.stopPropagation(); addToCart('庭院日晒咖啡豆', 108)">加入购物车</button>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------- 购物车 & 页脚 ----------------
st.markdown("""
<div class="section" id="cart">
  <h2 class="section-title">我的购物车</h2>
  <div style="background:#fff; padding:2rem; border-radius:16px; box-shadow:var(--card-shadow); text-align:center; color:#665c52;">
    <p style="font-size:1.1rem; margin-bottom:1rem;">🛒 当前共 <strong id="cart-count" style="color:var(--accent-brown); font-size:1.3rem;">0</strong> 件商品</p>
    <p style="font-size:0.9rem; opacity:0.8;">（演示模式：结算功能可无缝对接微信支付/Stripe）</p>
  </div>
</div>
<div class="footer" id="footer">
  <p>洋语楼咖啡 Yangyulou Coffee © 2024</p>
  <p style="margin-top:0.5rem; opacity:0.7;">杭州市西湖区龙井路88号 · hello@yangyulou.coffee · 0571-8888 6666</p>
</div>
""", unsafe_allow_html=True)

# ---------------- JavaScript 交互逻辑 ----------------
st.markdown("""
<script>
  let cartCount = 0;
  let cartItems = [];

  function addToCart(name, price) {
    cartCount++;
    cartItems.push({ name, price });
    document.getElementById('cart-count').textContent = cartCount;

    const toast = document.getElementById('cart-toast');
    toast.textContent = `✅ ${name} 已加入购物车 (共 ${cartCount} 件)`;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2500);
  }

  // 平滑滚动锚点
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
    });
  });
</script>
<div id="cart-toast" class="cart-toast"></div>
""", unsafe_allow_html=True)
