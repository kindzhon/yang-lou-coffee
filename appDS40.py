import streamlit as st

# 页面配置
st.set_page_config(
    page_title="洋语楼咖啡 | 艺术咖啡品牌",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隐藏 Streamlit 默认样式
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        margin: 0;
        padding: 0;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 自定义 CSS
custom_css = """
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
        font-family: 'Georgia', 'Noto Serif SC', serif;
        background-color: var(--cream);
        color: var(--text-dark);
        line-height: 1.7;
    }
    
    .stApp {
        background: linear-gradient(160deg, #FFFBF6 0%, #F5EDE3 30%, #F0DFD4 60%, #FDF5F0 100%);
    }
    
    /* 花瓣动画 */
    @keyframes petalFall {
        0% {
            transform: translateY(-10px) rotate(0deg) translateX(0px);
            opacity: 0;
        }
        10% {
            opacity: 0.7;
        }
        90% {
            opacity: 0.1;
        }
        100% {
            transform: translateY(100vh) rotate(360deg) translateX(30px);
            opacity: 0;
        }
    }
    
    .petal {
        position: fixed;
        pointer-events: none;
        z-index: 1000;
        animation: petalFall linear infinite;
    }
    
    .petal::before {
        content: '🌸';
        font-size: 20px;
        opacity: 0.6;
    }
    
    /* 导航按钮样式 */
    .nav-button {
        background: rgba(139, 94, 60, 0.1);
        color: #5C3A21;
        border: 1px solid #E8D5C4;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .nav-button:hover {
        background: rgba(139, 94, 60, 0.2);
        border-color: #8B5E3C;
    }
    
    /* 商品卡片 */
    .product-card {
        background: #FFFDF9;
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(60, 36, 21, 0.06);
        transition: all 0.35s ease;
        border: 1px solid transparent;
        text-align: center;
        height: 100%;
    }
    
    .product-card:hover {
        box-shadow: 0 14px 40px rgba(60, 36, 21, 0.16);
        transform: translateY(-4px);
        border-color: #E8D5C4;
    }
    
    .product-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .product-name {
        font-size: 1.3rem;
        color: #3C2415;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .product-desc {
        color: #8B6B5A;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        min-height: 50px;
    }
    
    .product-price {
        font-size: 1.8rem;
        color: #8B5E3C;
        font-weight: bold;
        margin: 1rem 0;
    }
    
    .product-price .unit {
        font-size: 0.9rem;
        color: #8B6B5A;
        font-weight: normal;
    }
    
    .tag {
        display: inline-block;
        background: rgba(196, 168, 130, 0.2);
        color: #8B5E3C;
        padding: 0.25rem 0.7rem;
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 0.2rem;
    }
    
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        margin: 2rem auto;
        max-width: 1200px;
        background: linear-gradient(160deg, #FFFBF6 0%, #F5EDE3 100%);
        border-radius: 32px;
        box-shadow: 0 4px 20px rgba(60, 36, 21, 0.06);
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(196, 168, 130, 0.2);
        color: #8B5E3C;
        padding: 0.5rem 1.5rem;
        border-radius: 30px;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }
    
    .hero-title {
        font-size: 3.5rem;
        color: #3C2415;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #8B6B5A;
        margin-bottom: 2rem;
    }
    
    .custom-button {
        background: #8B5E3C;
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 30px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 1rem;
    }
    
    .custom-button:hover {
        background: #5C3A21;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(92, 58, 33, 0.3);
    }
    
    .cart-item {
        padding: 1rem;
        border-bottom: 1px solid #E8D5C4;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .toast-message {
        position: fixed;
        top: 20px;
        right: 20px;
        background: #5a8a5a;
        color: white;
        padding: 1rem 2rem;
        border-radius: 30px;
        z-index: 9999;
        animation: slideIn 0.3s ease;
    }
    
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# 花瓣动画 HTML
petals_html = """
<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 999; overflow: hidden;">
"""
import random
for i in range(15):
    left = random.randint(0, 100)
    delay = random.uniform(0, 8)
    duration = random.uniform(10, 20)
    petals_html += f"""
    <div class="petal" style="
        left: {left}%;
        animation-delay: {delay}s;
        animation-duration: {duration}s;
    "></div>
    """
petals_html += "</div>"

st.markdown(petals_html, unsafe_allow_html=True)

# 商品数据
if 'products' not in st.session_state:
    st.session_state.products = [
        {"id": 1, "name": "洋语楼·经典手冲", "icon": "☕", "desc": "精选埃塞俄比亚耶加雪菲，手工慢冲，果酸明亮，回味甘甜。", "tags": ["手冲", "果香", "经典"], "price": 38, "unit": "/杯"},
        {"id": 2, "name": "玫瑰拿铁", "icon": "🌹", "desc": "意式浓缩遇见玫瑰花瓣，丝滑奶泡中绽放花香，温柔了整个午后。", "tags": ["拿铁", "花香", "人气"], "price": 42, "unit": "/杯"},
        {"id": 3, "name": "哥伦比亚单品豆", "icon": "🫘", "desc": "哥伦比亚慧兰产区，中度烘焙，坚果与可可风味，回韵悠长。", "tags": ["单品", "坚果", "精品"], "price": 88, "unit": "/袋(250g)"},
        {"id": 4, "name": "花语冷萃", "icon": "🧊", "desc": "12小时低温萃取，融入桂花与栀子花香，清爽中透着丝丝甜蜜。", "tags": ["冷萃", "花香", "夏日"], "price": 36, "unit": "/瓶"},
        {"id": 5, "name": "桂花燕麦拿铁", "icon": "🥛", "desc": "植物基燕麦奶搭配桂花糖浆，乳糖不耐友好，秋日氛围感满分。", "tags": ["植物基", "桂花", "健康"], "price": 40, "unit": "/杯"},
        {"id": 6, "name": "精品挂耳礼盒", "icon": "🎁", "desc": "六款风味挂耳包，精美礼盒装，送礼自用皆是品味之选。", "tags": ["礼盒", "挂耳", "送礼"], "price": 128, "unit": "/盒"},
    ]

if 'cart' not in st.session_state:
    st.session_state.cart = []

if 'show_toast' not in st.session_state:
    st.session_state.show_toast = False
    st.session_state.toast_message = ""

# 导航栏
col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
with col1:
    st.markdown("### ☕ 洋语楼咖啡")
with col3:
    if st.button("🏠 首页", key="nav_home", use_container_width=True):
        st.session_state.page = "home"
with col4:
    if st.button("🛍️ 商品", key="nav_products", use_container_width=True):
        st.session_state.page = "products"
with col5:
    cart_count = sum(item['quantity'] for item in st.session_state.cart)
    if st.button(f"🛒 购物车({cart_count})", key="nav_cart", use_container_width=True):
        st.session_state.page = "cart"

st.markdown("<hr style='border-color: #E8D5C4; margin: 0.5rem 0;'>", unsafe_allow_html=True)

# 初始化页面
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Toast 提示
if st.session_state.show_toast:
    st.markdown(f"""
    <div class="toast-message" id="toast">
        {st.session_state.toast_message}
    </div>
    <script>
        setTimeout(function() {{
            var toast = document.getElementById('toast');
            if(toast) toast.style.display = 'none';
        }}, 2000);
    </script>
    """, unsafe_allow_html=True)
    st.session_state.show_toast = False

# 首页
if st.session_state.page == "home":
    # Hero 区域
    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge">✦ 艺术咖啡品牌 ✦</div>
        <h1 class="hero-title">洋语楼 咖啡</h1>
        <p class="hero-subtitle">
            在咖啡豆与花瓣交织的香气里，<br>寻一段属于自己的静谧时光。
        </p>
        <button class="custom-button" onclick="document.querySelector('button[key=nav_products]').click()">
            探索我们的咖啡
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    # 商品预览
    st.markdown("<h2 style='text-align: center; color: #3C2415; margin: 2rem 0;'>✨ 精选推荐</h2>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    for idx, product in enumerate(st.session_state.products[:3]):
        with cols[idx]:
            st.markdown(f"""
            <div class="product-card">
                <div class="product-icon">{product['icon']}</div>
                <div class="product-name">{product['name']}</div>
                <div class="product-desc">{product['desc']}</div>
                <div>
                    {' '.join([f'<span class="tag">{tag}</span>' for tag in product['tags']])}
                </div>
                <div class="product-price">¥{product['price']} <span class="unit">{product['unit']}</span></div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"加入购物车 - {product['name']}", key=f"home_add_{product['id']}", use_container_width=True):
                cart_item = next((item for item in st.session_state.cart if item['id'] == product['id']), None)
                if cart_item:
                    cart_item['quantity'] += 1
                else:
                    st.session_state.cart.append({
                        "id": product['id'],
                        "name": product['name'],
                        "price": product['price'],
                        "unit": product['unit'],
                        "quantity": 1
                    })
                st.session_state.toast_message = f"✅ 已添加：{product['name']}"
                st.session_state.show_toast = True
                st.rerun()
    
    # 品牌故事
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; padding: 3rem; background: linear-gradient(180deg, #FFFBF6 0%, #FDF5F0 100%); border-radius: 32px; margin: 2rem auto; max-width: 1200px;">
        <h2 style="color: #3C2415; margin-bottom: 1rem;">🌸 洋语楼的故事</h2>
        <p style="color: #8B6B5A; font-size: 1.1rem; line-height: 2;">
            洋语楼咖啡，诞生于对咖啡艺术的热爱。<br>
            从哥伦比亚高原到埃塞俄比亚山谷，我们精心挑选每一颗咖啡豆，<br>
            用匠心烘焙，以花香为伴，将自然的馈赠融入每一杯之中。
        </p>
    </div>
    """, unsafe_allow_html=True)

# 商品页
elif st.session_state.page == "products":
    st.markdown("<h2 style='text-align: center; color: #3C2415; margin: 2rem 0;'>🛍️ 精选咖啡与好物</h2>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    for idx, product in enumerate(st.session_state.products):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="product-card">
                <div class="product-icon">{product['icon']}</div>
                <div class="product-name">{product['name']}</div>
                <div class="product-desc">{product['desc']}</div>
                <div>
                    {' '.join([f'<span class="tag">{tag}</span>' for tag in product['tags']])}
                </div>
                <div class="product-price">¥{product['price']} <span class="unit">{product['unit']}</span></div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"加入购物车", key=f"product_add_{product['id']}", use_container_width=True):
                cart_item = next((item for item in st.session_state.cart if item['id'] == product['id']), None)
                if cart_item:
                    cart_item['quantity'] += 1
                else:
                    st.session_state.cart.append({
                        "id": product['id'],
                        "name": product['name'],
                        "price": product['price'],
                        "unit": product['unit'],
                        "quantity": 1
                    })
                st.session_state.toast_message = f"✅ 已添加：{product['name']}"
                st.session_state.show_toast = True
                st.rerun()

# 购物车页
elif st.session_state.page == "cart":
    st.markdown("<h2 style='text-align: center; color: #3C2415; margin: 2rem 0;'>🛒 您的购物车</h2>", unsafe_allow_html=True)
    
    if len(st.session_state.cart) == 0:
        st.markdown("<p style='text-align: center; color: #8B6B5A; padding: 3rem;'>✨ 购物车是空的，去挑选心仪的咖啡吧~</p>", unsafe_allow_html=True)
        if st.button("去逛逛", use_container_width=True):
            st.session_state.page = "products"
            st.rerun()
    else:
        total = 0
        for idx, item in enumerate(st.session_state.cart):
            col1, col2, col3, col4, col5 = st.columns([0.5, 3, 1, 1, 1])
            with col1:
                st.markdown(f"### {item.get('icon', '☕')}")
            with col2:
                st.markdown(f"**{item['name']}**")
                st.caption(f"{item['unit']}")
            with col3:
                st.markdown(f"¥{item['price']}")
            with col4:
                qty_col1, qty_col2, qty_col3 = st.columns([1, 1, 1])
                with qty_col1:
                    if st.button("➖", key=f"minus_{idx}"):
                        st.session_state.cart[idx]['quantity'] -= 1
                        if st.session_state.cart[idx]['quantity'] <= 0:
                            st.session_state.cart.pop(idx)
                        st.rerun()
                with qty_col2:
                    st.markdown(f"**{item['quantity']}**")
                with qty_col3:
                    if st.button("➕", key=f"plus_{idx}"):
                        st.session_state.cart[idx]['quantity'] += 1
                        st.rerun()
            with col5:
                st.markdown(f"**¥{item['price'] * item['quantity']}**")
            
            total += item['price'] * item['quantity']
        
        st.markdown(f"<h2 style='text-align: right; color: #3C2415; margin-top: 2rem;'>总计：¥{total}</h2>", unsafe_allow_html=True)
        
        # 结账表单
        st.markdown("---")
        st.markdown("### 📝 填写订单信息")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("您的姓名", key="customer_name")
        with col2:
            phone = st.text_input("联系电话", key="customer_phone")
        note = st.text_area("备注（选填）", key="customer_note")
        
        if st.button("✨ 提交订单", use_container_width=True):
            if not name or not phone:
                st.error("请填写姓名和联系电话")
            else:
                # 这里可以发送订单数据
                order_details = []
                for item in st.session_state.cart:
                    order_details.append(f"{item['name']} × {item['quantity']} = ¥{item['price'] * item['quantity']}")
                
                st.success("🎉 订单已提交！我们会尽快联系您～")
                print(f"新订单: {name}, {phone}, 备注: {note}")
                print("订单明细:", order_details)
                
                # 清空购物车
                st.session_state.cart = []
                
                # 延迟跳转
                import time
                time.sleep(1)
                st.session_state.page = "home"
                st.rerun()

# 页脚
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #8B6B5A; border-top: 1px solid #E8D5C4; margin-top: 2rem;">
    <h3 style="color: #3C2415;">☕ 洋语楼咖啡</h3>
    <p>咖啡 · 豆香 · 花语 | 艺术咖啡品牌</p>
    <p style="font-size: 0.8rem;">© 2024 洋语楼咖啡 YangYuLou Coffee. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
