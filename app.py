import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# 页面配置
st.set_page_config(
    page_title="洋语楼咖啡 | Yangyu Lou Coffee",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 初始化 Session State
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'total' not in st.session_state:
    st.session_state.total = 0

# 自定义 CSS - 现代柔和艺术风格
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Noto+Sans+SC:wght@300;400;500&display=swap');
    
    /* 全局样式 */
    .stApp {
        background: linear-gradient(135deg, #faf8f5 0%, #f5ebe0 50%, #faf7f2 100%);
        font-family: 'Noto Sans SC', sans-serif;
    }
    
    /* 标题字体 */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #5c4033;
    }
    
    /* 导航栏样式 */
    .nav-container {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        padding: 1rem 2rem;
        border-radius: 0 0 20px 20px;
        box-shadow: 0 4px 20px rgba(139, 69, 19, 0.1);
        margin-bottom: 2rem;
    }
    
    /* 英雄区域 */
    .hero {
        background: linear-gradient(rgba(92, 64, 51, 0.3), rgba(139, 69, 19, 0.2)), 
                    url('https://images.unsplash.com/photo-1447933601403-0c6688de543e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        padding: 8rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,182,193,0.1) 0%, transparent 70%);
        animation: float 20s infinite linear;
    }
    
    @keyframes float {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .hero-title {
        font-size: 3.5rem;
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #fff8f0;
        font-style: italic;
        position: relative;
        z-index: 1;
    }
    
    /* 产品卡片 */
    .product-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(139, 69, 19, 0.08);
        transition: all 0.3s ease;
        border: 1px solid rgba(139, 69, 19, 0.1);
        height: 100%;
    }
    
    .product-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(139, 69, 19, 0.15);
    }
    
    .product-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    
    .flower-tag {
        display: inline-block;
        background: linear-gradient(135deg, #ffe4e1 0%, #fff0f5 100%);
        color: #8b4513;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        border: 1px solid rgba(139, 69, 19, 0.2);
    }
    
    /* 按钮样式 */
    .stButton>button {
        background: linear-gradient(135deg, #8b6914 0%, #a0522d 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 500;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(139, 69, 19, 0.3);
    }
    
    /* 购物车徽章 */
    .cart-badge {
        background: #e74c3c;
        color: white;
        border-radius: 50%;
        padding: 0.2rem 0.6rem;
        font-size: 0.8rem;
        position: relative;
        top: -10px;
        left: -5px;
    }
    
    /* 特色区域 */
    .feature-section {
        background: white;
        border-radius: 20px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }
    
    /* 分隔线 */
    .floral-divider {
        text-align: center;
        margin: 3rem 0;
        font-size: 1.5rem;
        color: #d4a373;
    }
    
    /* 柔和文字效果 */
    .soft-text {
        color: #6b4423;
        line-height: 1.8;
    }
    
    /* 隐藏默认菜单 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 响应式 */
    @media (max-width: 768px) {
        .hero-title { font-size: 2rem; }
        .hero { padding: 4rem 1rem; }
    }
</style>
""", unsafe_allow_html=True)

# 数据：咖啡产品
products = [
    {
        "id": 1,
        "name": "春日花海 · 拿铁",
        "price": 42,
        "description": "帕卡拉玛咖啡豆，融入橙蜜、桔子与柠檬草香",
        "flowers": ["洋甘菊", "薰衣草"],
        "image": "https://images.unsplash.com/photo-1541167760496-1628856ab772?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "roast": "浅中烘"
    },
    {
        "id": 2,
        "name": "玫瑰午后 · 摩卡",
        "price": 48,
        "description": "哥伦比亚豆配以大马士革玫瑰萃取，巧克力基调",
        "flowers": ["玫瑰", "可可花"],
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "roast": "中烘"
    },
    {
        "id": 3,
        "name": "茉莉晨露 · 手冲",
        "price": 38,
        "description": "云南普洱豆，茉莉花窨制工艺，清新茶感",
        "flowers": ["茉莉", "茶花"],
        "image": "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "roast": "浅烘"
    },
    {
        "id": 4,
        "name": "樱花纷飞 · 冷萃",
        "price": 45,
        "description": "肯尼亚AA级豆，樱花与莓果风味层次，低温慢萃12小时",
        "flowers": ["樱花", "覆盆子花"],
        "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "roast": "中深烘"
    },
    {
        "id": 5,
        "name": "桂花庭院 · 澳白",
        "price": 40,
        "description": "巴西喜拉多豆，金桂飘香，奶泡绵密如云朵",
        "flowers": ["桂花", "橙花"],
        "image": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "roast": "中烘"
    },
    {
        "id": 6,
        "name": "薰衣草梦境 · 康宝蓝",
        "price": 46,
        "description": "危地马拉安提瓜豆，薰衣草精油点缀，奶油甜美",
        "flowers": ["薰衣草", "香草花"],
        "image": "https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "roast": "中深烘"
    }
]

# 导航栏
cols = st.columns([1, 4, 1])
with cols[1]:
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem;">
        <div style="font-family: 'Playfair Display', serif; font-size: 1.8rem; color: #5c4033; font-weight: 600;">
            🌸 洋语楼
        </div>
        <div style="display: flex; gap: 2rem;">
            <a href="#home" style="text-decoration: none; color: #6b4423; font-weight: 500;">首页</a>
            <a href="#shop" style="text-decoration: none; color: #6b4423; font-weight: 500;">臻选豆单</a>
            <a href="#about" style="text-decoration: none; color: #6b4423; font-weight: 500;">品牌故事</a>
            <a href="#cart" style="text-decoration: none; color: #6b4423; font-weight: 500;">购物车({})</a>
        </div>
    </div>
    """.format(len(st.session_state.cart)), unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero" id="home">
    <div class="hero-title">洋语楼咖啡</div>
    <div class="hero-subtitle">Blossoms & Beans · 花与咖啡豆的私语</div>
    <br>
    <div style="color: #fff8f0; font-size: 1rem; margin-top: 2rem;">
        每一杯都是花朵与咖啡豆的浪漫邂逅
    </div>
</div>
""", unsafe_allow_html=True)

# 品牌价值主张
st.markdown("""
<div style="text-align: center; padding: 2rem; max-width: 800px; margin: 0 auto;">
    <h2 style="color: #5c4033; margin-bottom: 1rem;">自然之艺，手工之心</h2>
    <p class="soft-text" style="font-size: 1.1rem;">
        洋语楼相信，咖啡不仅是提神的饮品，更是一场感官的艺术之旅。
        我们从世界各地甄选精品咖啡豆，结合东方花卉工艺，<br>
        让每一口呼吸都伴随着花香与咖啡香的交织。
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="floral-divider">✿ ✿ ✿</div>', unsafe_allow_html=True)

# 产品展示区域
st.markdown('<h2 style="text-align: center; color: #5c4033; margin-bottom: 3rem;" id="shop">季节限定 · 花语系列</h2>', unsafe_allow_html=True)

# 创建产品网格
cols_per_row = 3
for i in range(0, len(products), cols_per_row):
    cols = st.columns(cols_per_row)
    for idx, col in enumerate(cols):
        if i + idx < len(products):
            product = products[i + idx]
            with col:
                st.markdown(f"""
                <div class="product-card">
                    <img src="{product['image']}" class="product-image">
                    <div style="margin-bottom: 0.5rem;">
                        {''.join([f'<span class="flower-tag">🌸 {f}</span>' for f in product['flowers']])}
                    </div>
                    <h3 style="margin: 0.5rem 0; color: #5c4033; font-size: 1.3rem;">{product['name']}</h3>
                    <p style="color: #8b6914; font-size: 0.9rem; margin: 0.5rem 0;">
                        <span style="background: #f5ebe0; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem;">{product['roast']}</span>
                    </p>
                    <p style="color: #666; font-size: 0.95rem; line-height: 1.5; min-height: 50px;">
                        {product['description']}
                    </p>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
                        <span style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #8b4513; font-weight: 600;">
                            ¥{product['price']}
                        </span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"加入购物车", key=f"btn_{product['id']}"):
                    st.session_state.cart.append(product)
                    st.session_state.total += product['price']
                    st.balloons()
                    st.success(f"已添加 {product['name']} 到购物车！")

# 品牌故事
st.markdown('<div class="floral-divider">✿ ✿ ✿</div>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: #5c4033; margin-bottom: 2rem;" id="about">品牌故事</h2>', unsafe_allow_html=True)

story_col1, story_col2 = st.columns([1, 1])
with story_col1:
    st.markdown("""
    <div class="feature-section">
        <h3 style="color: #8b6914; margin-bottom: 1rem;">从一颗生豆到满室花香</h3>
        <p class="soft-text">
            洋语楼诞生于2012年的春天。创始人曾在云南的花田与萨尔瓦多的圣伊莲娜蕾德拉咖啡庄园之间寻找灵感，
            发现花朵与咖啡豆在发酵过程中有着相似的化学美学——都是时间与自然的魔法。
        </p>
        <p class="soft-text">
            我们独创的"花香冷萃工艺"，将食用级鲜花与精品咖啡豆共同低温发酵，
            既保留了咖啡的醇厚，又赋予了清雅的芬芳。
        </p>
        <br>
        <div style="background: #faf8f5; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #d4a373;">
            <p style="font-style: italic; color: #6b4423; margin: 0;">
                "咖啡是液体的阳光，花朵是固态的香气，<br>
                而洋语楼，是两者相遇的楼阁。"
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with story_col2:
    # 使用占位图或Unsplash图片
    st.image("https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", 
             caption="洋语楼咖啡工作室 · 深圳华侨城OCT", 
             use_column_width=True)

# 购物车侧边栏
with st.sidebar:
    st.markdown("""
    <div style="padding: 1rem; background: white; border-radius: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
        <h3 style="color: #5c4033; margin-bottom: 1rem;">🛒 购物车</h3>
    """, unsafe_allow_html=True)
    
    if not st.session_state.cart:
        st.markdown('<p style="color: #999; font-style: italic;">购物车还是空的...</p>', unsafe_allow_html=True)
    else:
        for item in st.session_state.cart:
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; 
                        padding: 0.8rem; background: #faf8f5; border-radius: 8px; margin-bottom: 0.5rem;">
                <div>
                    <div style="font-weight: 500; color: #5c4033;">{item['name']}</div>
                    <div style="font-size: 0.8rem; color: #999;">{' '.join(item['flowers'])}</div>
                </div>
                <div style="color: #8b4513; font-weight: 600;">¥{item['price']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="border-top: 2px solid #f0e6dc; margin-top: 1rem; padding-top: 1rem;">
            <div style="display: flex; justify-content: space-between; font-size: 1.2rem; font-weight: 600; color: #5c4033;">
                <span>总计</span>
                <span>¥{st.session_state.total}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🌸 结算购买", key="checkout"):
            st.success("感谢您的订购！我们将尽快为您配送这份花香与咖啡的美好。")
            st.session_state.cart = []
            st.session_state.total = 0
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 联系了局信息
    st.markdown("""
    <div style="margin-top: 2rem; padding: 1.5rem; background: #f5ebe0; border-radius: 16px; text-align: center;">
        <h4 style="color: #5c4033; margin-bottom: 0.5rem;">联系我们</h4>
        <p style="color: #6b4423; font-size: 0.9rem; margin: 0.3rem 0;">
            📍 上海市徐汇区安福路198号<br>
            📧 hello@yangyulou.coffee<br>
            📞 021-6433-xxxx
        </p>
        <div style="margin-top: 1rem; font-size: 1.2rem;">
            <span style="margin: 0 0.3rem;">📷</span>
            <span style="margin: 0 0.3rem;">🍠</span>
            <span style="margin: 0 0.3rem;">🎵</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 页脚
st.markdown("""
<div style="text-align: center; padding: 3rem 1rem; margin-top: 3rem; color: #999; font-size: 0.9rem;">
    <div style="margin-bottom: 1rem;">✿ ✿ ✿</div>
    <p>&copy; 2024 洋语楼咖啡 Yangyu Lou Coffee. All rights reserved.</p>
    <p style="font-size: 0.8rem; margin-top: 0.5rem;">Designed with ☕ & 🌸 in Shanghai</p>
</div>
""", unsafe_allow_html=True)

# 浮动购物车按钮（移动端友好）
if len(st.session_state.cart) > 0:
    st.markdown(f"""
    <div style="position: fixed; bottom: 30px; right: 30px; z-index: 1000;">
        <a href="#cart" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #8b6914, #a0522d); 
                        color: white; padding: 1rem 1.5rem; border-radius: 50px; 
                        box-shadow: 0 4px 15px rgba(139,69,19,0.3); display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 1.2rem;">🛒</span>
                <span style="font-weight: 600;">{len(st.session_state.cart)} 件商品</span>
                <span style="background: rgba(255,255,255,0.2); padding: 0.2rem 0.6rem; border-radius: 20px;">
                    ¥{st.session_state.total}
                </span>
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)
