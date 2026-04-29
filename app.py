import streamlit as st

# ---------------- 基础配置 ----------------
st.set_page_config(
    page_title="洋语楼咖啡",
    page_icon="☕",
    layout="wide"
)

# ---------------- 自定义样式 ----------------
st.markdown(
    """
    <style>
    /* 全局字体与背景 */
    html, body, [class*="css"]  {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif;
        background: radial-gradient(circle at top left, #fdf4ea 0, #f7ebe4 35%, #f3e7f0 70%, #f7f5f2 100%);
        color: #3b2b2b;
    }

    /* 去掉顶部多余空白 */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    /* 导航栏 */
    .yy-nav {
        position: sticky;
        top: 0;
        z-index: 999;
        backdrop-filter: blur(16px);
        background: rgba(253, 244, 234, 0.85);
        border-radius: 999px;
        padding: 0.4rem 1.2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border: 1px solid rgba(120, 90, 70, 0.12);
        box-shadow: 0 14px 40px rgba(0,0,0,0.04);
        margin-bottom: 1.5rem;
    }

    .yy-nav-left {
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }

    .yy-logo {
        width: 32px;
        height: 32px;
        border-radius: 999px;
        background: radial-gradient(circle at 30% 20%, #fef6e9 0, #f0d2b0 40%, #c28b5b 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.12);
    }

    .yy-brand-cn {
        font-weight: 600;
        letter-spacing: 0.12em;
        font-size: 0.85rem;
    }

    .yy-brand-en {
        font-size: 0.7rem;
        opacity: 0.7;
    }

    .yy-nav-links {
        display: flex;
        gap: 0.8rem;
        font-size: 0.8rem;
    }

    .yy-nav-link {
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        cursor: pointer;
        border: 1px solid transparent;
        transition: all 0.18s ease-out;
        color: #5a4337;
        text-decoration: none;
    }

    .yy-nav-link:hover {
        background: rgba(255,255,255,0.9);
        border-color: rgba(120, 90, 70, 0.25);
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }

    .yy-nav-link-primary {
        background: linear-gradient(135deg, #c58b5b, #b46b5a);
        color: #fff !important;
        box-shadow: 0 10px 24px rgba(180, 107, 90, 0.35);
    }

    .yy-nav-link-primary:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 30px rgba(180, 107, 90, 0.45);
    }

    /* 主视觉区 */
    .yy-hero {
        display: grid;
        grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr);
        gap: 3rem;
        align-items: center;
        margin: 1.5rem 0 2.5rem 0;
    }

    @media (max-width: 900px) {
        .yy-hero {
            grid-template-columns: minmax(0, 1fr);
        }
    }

    .yy-hero-title-cn {
        font-size: 2.6rem;
        line-height: 1.15;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 0.6rem;
    }

    .yy-hero-title-en {
        font-size: 0.9rem;
        letter-spacing: 0.28em;
        text-transform: uppercase;
        opacity: 0.7;
        margin-bottom: 1.2rem;
    }

    .yy-hero-sub {
        font-size: 1rem;
        line-height: 1.7;
        max-width: 32rem;
        opacity: 0.9;
        margin-bottom: 1.6rem;
    }

    .yy-hero-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1.8rem;
    }

    .yy-tag {
        padding: 0.25rem 0.7rem;
        border-radius: 999px;
        border: 1px solid rgba(120, 90, 70, 0.25);
        font-size: 0.75rem;
        background: rgba(255,255,255,0.7);
        backdrop-filter: blur(10px);
    }

    .yy-hero-cta {
        display: flex;
        flex-wrap: wrap;
        gap: 0.7rem;
        align-items: center;
    }

    .yy-hero-note {
        font-size: 0.75rem;
        opacity: 0.7;
    }

    .yy-hero-art {
        position: relative;
        min-height: 260px;
    }

    .yy-hero-card-main {
        position: absolute;
        inset: 0;
        margin: auto;
        width: 100%;
        max-width: 360px;
        height: 260px;
        border-radius: 32px;
        background: radial-gradient(circle at 20% 0, #fffaf4 0, #f3e0d0 40%, #c58b5b 100%);
        box-shadow: 0 26px 60px rgba(0,0,0,0.25);
        padding: 1.4rem 1.6rem;
        color: #2f1f1a;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .yy-hero-card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .yy-hero-badge {
        padding: 0.25rem 0.7rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.85);
        font-size: 0.7rem;
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
    }

    .yy-hero-coffee {
        font-size: 2.4rem;
    }

    .yy-hero-card-body {
        font-size: 0.85rem;
        line-height: 1.6;
        max-width: 14rem;
    }

    .yy-hero-card-footer {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        font-size: 0.75rem;
    }

    .yy-hero-beans {
        font-size: 1.6rem;
    }

    .yy-hero-flower {
        font-size: 1.6rem;
    }

    .yy-hero-floating {
        position: absolute;
        width: 120px;
        height: 120px;
        border-radius: 32px;
        background: rgba(255,255,255,0.9);
        box-shadow: 0 18px 40px rgba(0,0,0,0.18);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
    }

    .yy-hero-floating.left {
        left: -10px;
        bottom: -10px;
    }

    .yy-hero-floating.right {
        right: -10px;
        top: -10px;
    }

    /* 区块标题 */
    .yy-section-title {
        font-size: 1.4rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }

    .yy-section-sub {
        font-size: 0.9rem;
        opacity: 0.7;
        margin-bottom: 1.4rem;
    }

    /* 商品卡片 */
    .yy-product-card {
        border-radius: 24px;
        padding: 1.2rem 1.3rem;
        background: rgba(255,255,255,0.9);
        box-shadow: 0 18px 40px rgba(0,0,0,0.06);
        border: 1px solid rgba(120, 90, 70, 0.12);
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
        height: 100%;
    }

    .yy-product-topline {
        font-size: 0.7rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        opacity: 0.6;
    }

    .yy-product-name {
        font-size: 1.05rem;
        font-weight: 600;
    }

    .yy-product-notes {
        font-size: 0.8rem;
        opacity: 0.85;
    }

    .yy-product-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.35rem;
        font-size: 0.7rem;
    }

    .yy-product-tag {
        padding: 0.15rem 0.55rem;
        border-radius: 999px;
        background: rgba(245, 232, 220, 0.9);
    }

    .yy-product-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 0.4rem;
    }

    .yy-price {
        font-weight: 600;
        font-size: 0.95rem;
    }

    .yy-gram {
        font-size: 0.7rem;
        opacity: 0.7;
    }

    .yy-buy-btn {
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        border: none;
        background: linear-gradient(135deg, #c58b5b, #b46b5a);
        color: #fff;
        font-size: 0.8rem;
        cursor: pointer;
        box-shadow: 0 10px 24px rgba(180, 107, 90, 0.35);
        transition: all 0.18s ease-out;
    }

    .yy-buy-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 30px rgba(180, 107, 90, 0.45);
    }

    /* 购买模块 */
    .yy-checkout-box {
        border-radius: 24px;
        padding: 1.4rem 1.5rem;
        background: rgba(255,255,255,0.95);
        box-shadow: 0 18px 40px rgba(0,0,0,0.08);
        border: 1px solid rgba(120, 90, 70, 0.16);
    }

    .yy-checkout-title {
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 0.4rem;
    }

    .yy-checkout-sub {
        font-size: 0.8rem;
        opacity: 0.75;
        margin-bottom: 0.8rem;
    }

    .yy-checkout-summary {
        font-size: 0.85rem;
        margin-top: 0.8rem;
        padding-top: 0.6rem;
        border-top: 1px dashed rgba(120, 90, 70, 0.25);
    }

    .yy-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
        background: rgba(245, 232, 220, 0.9);
        font-size: 0.7rem;
        margin-right: 0.3rem;
        margin-bottom: 0.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- 导航栏 ----------------
nav_html = """
<div class="yy-nav">
  <div class="yy-nav-left">
    <div class="yy-logo">☕</div>
    <div>
      <div class="yy-brand-cn">洋语楼咖啡</div>
      <div class="yy-brand-en">YANG YU LOU COFFEE</div>
    </div>
  </div>
  <div class="yy-nav-links">
    <a class="yy-nav-link" href="#hero">主视觉</a>
    <a class="yy-nav-link" href="#products">咖啡豆</a>
    <a class="yy-nav-link" href="#checkout">下单</a>
    <a class="yy-nav-link yy-nav-link-primary" href="#checkout">立即品尝</a>
  </div>
</div>
"""

st.markdown(nav_html, unsafe_allow_html=True)

# ---------------- 主视觉区 ----------------
st.markdown('<div id="hero"></div>', unsafe_allow_html=True)

col_hero_left, col_hero_right = st.columns([1.2, 1])

with col_hero_left:
    st.markdown(
        """
        <div class="yy-hero">
          <div>
            <div class="yy-hero-title-en">SLOW ROASTED · FLOWER NOTES</div>
            <div class="yy-hero-title-cn">洋语楼里的<br/>一杯柔软咖啡</div>
            <div class="yy-hero-sub">
              在洋语楼，我们把咖啡豆当作一束花来雕琢——
              让烘焙的层次、花香的细节、果酸的起伏，在你的味蕾上缓慢展开。
            </div>
            <div class="yy-hero-tags">
              <span class="yy-tag">单一产区 · 手工烘焙</span>
              <span class="yy-tag">花香与果香并存</span>
              <span class="yy-tag">适合手冲 / 意式 / 冷萃</span>
            </div>
            <div class="yy-hero-cta">
              <button class="yy-buy-btn" onclick="window.location.hash='#checkout'">选一款今日咖啡</button>
              <div class="yy-hero-note">每日限量小批次烘焙 · 为今天的心情准备</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_hero_right:
    st.markdown(
        """
        <div class="yy-hero-art">
          <div class="yy-hero-card-main">
            <div class="yy-hero-card-header">
              <div class="yy-hero-badge">
                <span>今日风味</span>
                <span>✶</span>
              </div>
              <div class="yy-hero-coffee">☕</div>
            </div>
            <div class="yy-hero-card-body">
              花香调耶加雪菲，带白花、柑橘与蜂蜜的层次，
              适合一个慢下来的下午。
            </div>
            <div class="yy-hero-card-footer">
              <div>
                <div style="font-size:0.75rem; opacity:0.7;">TASTING NOTES</div>
                <div style="font-size:0.85rem;">白花 · 柑橘 · 蜂蜜</div>
              </div>
              <div>
                <div class="yy-hero-beans">🫘</div>
              </div>
            </div>
          </div>
          <div class="yy-hero-floating left">
            <span class="yy-hero-flower">🌸</span>
          </div>
          <div class="yy-hero-floating right">
            <span>🫘</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- 商品数据 ----------------
products = [
    {
        "id": "yy01",
        "name": "花语耶加 · 日晒",
        "topline": "ETHIOPIA YIRGACHEFFE · NATURAL",
        "notes": "白花、熟莓果、蜂蜜甜感，酸质细腻，适合手冲与冷萃。",
        "tags": ["花香", "莓果", "冷萃友好"],
        "price": 98,
        "gram": 200
    },
    {
        "id": "yy02",
        "name": "晨光花园 · 混合豆",
        "topline": "HOUSE BLEND · FLORAL & NUTTY",
        "notes": "坚果、可可与淡淡花香，平衡顺滑，适合意式与拿铁。",
        "tags": ["坚果", "可可", "意式"],
        "price": 88,
        "gram": 250
    },
    {
        "id": "yy03",
        "name": "雨后玫瑰 · 水洗",
        "topline": "COLOMBIA · WASHED",
        "notes": "玫瑰花、柑橘与红糖尾韵，干净通透，适合手冲。",
        "tags": ["玫瑰", "柑橘", "干净"],
        "price": 102,
        "gram": 200
    }
]

# 初始化购物车
if "cart" not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(pid):
    st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + 1

# ---------------- 商品展示区 ----------------
st.markdown('<div id="products"></div>', unsafe_allow_html=True)
st.markdown('<div class="yy-section-title">COFFEE BEANS</div>', unsafe_allow_html=True)
st.markdown('<div class="yy-section-sub">为不同的日子，准备三种带花香的咖啡表情。</div>', unsafe_allow_html=True)

cols = st.columns(3)
for col, p in zip(cols, products):
    with col:
        st.markdown(
            f"""
            <div class="yy-product-card">
              <div class="yy-product-topline">{p["topline"]}</div>
              <div class="yy-product-name">{p["name"]}</div>
              <div class="yy-product-notes">{p["notes"]}</div>
              <div class="yy-product-tags">
                {''.join([f'<span class="yy-product-tag">{t}</span>' for t in p["tags"]])}
              </div>
              <div class="yy-product-footer">
                <div>
                  <div class="yy-price">¥ {p["price"]}</div>
                  <div class="yy-gram">{p["gram"]} g</div>
                </div>
                <div>
                  """,
            unsafe_allow_html=True
        )
        # 使用 Streamlit 按钮触发加入购物车
        if st.button("加入今日清单", key=f"btn_{p['id']}"):
            add_to_cart(p["id"])
            st.success(f"已加入：{p['name']}")

        st.markdown("</div></div>", unsafe_allow_html=True)

# ---------------- 购买 / 下单模块 ----------------
st.markdown('<div id="checkout"></div>', unsafe_allow_html=True)
st.markdown("---")

checkout_col_left, checkout_col_right = st.columns([1.2, 1])

with checkout_col_left:
    st.markdown(
        """
        <div class="yy-section-title">ORDER TODAY</div>
        <div class="yy-section-sub">
          选几款你今天想遇见的风味，我们会为你准备新鲜烘焙的咖啡豆。
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="yy-checkout-box">', unsafe_allow_html=True)
    st.markdown('<div class="yy-checkout-title">今日咖啡清单</div>', unsafe_allow_html=True)
    st.markdown('<div class="yy-checkout-sub">这不是正式支付页面，更像是你与自己的一份咖啡备忘录。</div>', unsafe_allow_html=True)

    if not st.session_state.cart:
        st.info("你的清单目前是空的，去上面挑一款咖啡豆吧。")
    else:
        total = 0
        for p in products:
            pid = p["id"]
            if pid in st.session_state.cart:
                qty = st.session_state.cart[pid]
                line_price = qty * p["price"]
                total += line_price
                st.markdown(
                    f"""
                    <div class="yy-pill">
                      <span>{p["name"]}</span>
                      <span>× {qty}</span>
                      <span>¥ {line_price}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown(
            f"""
            <div class="yy-checkout-summary">
              <div>预计金额：<strong>¥ {total}</strong></div>
              <div style="font-size:0.75rem; opacity:0.7; margin-top:0.3rem;">
                你可以截图或复制这份清单，通过线下门店 / 小程序 / 客服完成正式下单。
              </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

with checkout_col_right:
    st.markdown(
        """
        <div class="yy-checkout-box">
          <div class="yy-checkout-title">冲煮建议 · 小提示</div>
          <div class="yy-checkout-sub">
            每一杯咖啡，都是你与当下的一次对话。以下是一些温柔的起点：
          </div>
          <ul style="font-size:0.8rem; padding-left:1.1rem; line-height:1.7;">
            <li>第一次尝试花香豆，可以从手冲开始，水温 90–92℃ 更易感知香气层次。</li>
            <li>喜欢奶咖，可以选择带坚果与可可风味的混合豆，做成拿铁更顺滑。</li>
            <li>如果你习惯冷萃，建议选择酸质明亮、甜感清晰的豆子，并延长浸泡时间。</li>
          </ul>
          <div style="margin-top:0.8rem; font-size:0.8rem; opacity:0.8;">
            无论你今天的心情如何，愿这一杯咖啡，替你说一句温柔的话。
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )
