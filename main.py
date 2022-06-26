#!/usr/bin/env python
# coding: utf-8

# In[1]:


import telebot
from telebot import types


# In[2]:


token = 'telegram bot TOKEN'


# In[3]:


bot = telebot.TeleBot(token)


# In[4]:


print(bot.get_me())


# In[5]:


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Not really good :(', 'Great!')


# In[ ]:


@bot.message_handler(func = lambda message: message.text == '/start')
def send_text(message):
    bot.send_message(message.chat.id, 'Hi, dear!')
    bot.send_message(message.chat.id, 'How are you?', reply_markup=keyboard1)
@bot.message_handler(func = lambda message: message.text == 'Great!')
def send_text(message):
    bot.send_message(message.chat.id, 'Do you need any help with your subjects?')
    bot.send_message(message.chat.id, "Enter 'Start' and we will start")
@bot.message_handler(func = lambda message: message.text == 'Not really good :(')
def send_text(message):
    bot.send_message(message.chat.id, 'Whatever is happening in your life, you know, I can always help you!')
    bot.send_message(message.chat.id, 'Do you need any help with your subjects?')
    bot.send_message(message.chat.id, "Enter 'Start' and we will start")
        
        
@bot.message_handler(func = lambda message: message.text.lower() == 'start')
def send_text(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 
    keyboard.row('Management tools')   
    keyboard.row('Marketing tools') 
    keyboard.row('Financial tools')
    bot.send_message(message.chat.id, '*Please, choose a subject:*', reply_markup = keyboard, parse_mode = 'markdown')

# MANAGEMENT TOOLS    
@bot.message_handler(func = lambda message: message.text == 'Management tools')
def send_text(message):
    keyboard = telebot.types.ReplyKeyboardMarkup() 
    bot.send_message(message.chat.id, 'You have chosen management studies. Good choice!', reply_markup = keyboard, parse_mode = 'markdown')
    keyboard.row('SWOT-analysis')   
    keyboard.row("Porter's Five Forces")
    keyboard.row('Value Chain')
    keyboard.row('Ansoff matrix')
    keyboard.row('Start')
    bot.send_message(message.chat.id, '*Choose one among them:*', reply_markup = keyboard, parse_mode = 'markdown')
@bot.message_handler(func = lambda message: message.text == 'SWOT-analysis')
def send_text(message):
    bot.send_message(message.chat.id, "SWOT analysis is a business analysis process that ensures that objectives for a project are clearly defined and that all factors related to the project are properly identified. The SWOT analysis process involves four areas: Strengths, Weaknesses, Opportunities and Threats. Both internal and external components are considered when doing SWOT Analysis, as they both have the potential to impact the success of a project or venture.")
    bot.send_photo(chat_id = message.chat.id, photo = "http://asu-analitika.ru/wp-content/uploads/2019/10/swot-analysis-header1-1.png")
    bot.send_message(message.chat.id, "[Additional information:](https://www.mindtools.com/pages/article/newTMC_05.htm)", parse_mode='MarkdownV2')
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 
@bot.message_handler(func = lambda message: message.text == "Porter's Five Forces")
def send_text(message):
    bot.send_message(message.chat.id, "Porter's Five Forces of Competitive Position Analysis were developed in 1979 by Michael E Porter of Harvard Business School as a simple framework for assessing and evaluating the competitive strength and position of a business organisation. This theory is based on the concept that there are five forces that determine the competitive intensity and attractiveness of a market. Porter’s five forces help to identify where power lies in a business situation. This is useful both in understanding the strength of an organisation’s current competitive position, and the strength of a position that an organisation may look to move into. Strategic analysts often use Porter’s five forces to understand whether new products or services are potentially profitable. By understanding where power lies, the theory can also be used to identify areas of strength, to improve weaknesses and to avoid mistakes.")
    bot.send_photo(chat_id = message.chat.id, photo = "https://i2.wp.com/www.business-to-you.com/wp-content/uploads/2017/04/Five-Forces-Model-Porter.png?w=1361&ssl=1")
    bot.send_message(message.chat.id, "[Additional information:](https://www.businessnewsdaily.com/5446-porters-five-forces.html)", parse_mode='MarkdownV2')    
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 
@bot.message_handler(func = lambda message: message.text == "Value Chain")
def send_text(message):
    bot.send_message(message.chat.id, "Value chain analysis focuses on analyzing the internal activities of a business in an effort to understand costs, locate the activities that add the most value, and differentiate from the competition. To develop an analysis, Porter's model outlines primary business functions as the basic areas and activities of inbound logistics, operations, outbound logistics, marketing and sales, and service. The model also identifies the discrete tasks found in the important support activities of firm infrastructure, human resources management, technology, and procurement. The overall goal of value chain analysis it to identify areas and activities that will benefit from change in order to improve profitability and efficiency.")
    bot.send_message(message.chat.id, "[Additional information:](https://www.visual-paradigm.com/guide/strategic-analysis/what-is-value-chain-analysis/)", parse_mode='MarkdownV2')        
    bot.send_photo(chat_id = message.chat.id, photo = "https://i1.wp.com/www.business-to-you.com/wp-content/uploads/2018/03/Value-Chain-1.png?w=1198&ssl=1")
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 
@bot.message_handler(func = lambda message: message.text == 'Ansoff matrix')
def send_text(message):
    bot.send_message(message.chat.id, "This model is essential for strategic marketing planning where it can be applied to look at opportunities to grow revenue for a business through developing new products and services or 'tapping into' new markets. So it's sometimes known as the ‘Product-Market Matrix’ instead of the ‘Ansoff Matrix’. This focus on growth means that it's one of the most widely used marketing models. It is used to evaluate opportunities for  companies to increase their sales through showing alternative combinations for new markets (i.e. customer segments and geographical locations) against products and services offering four strategies as shown.")
    bot.send_message(message.chat.id, "[Additional information:](https://blog.oxfordcollegeofmarketing.com/2016/08/01/using-ansoff-matrix-develop-marketing-strategy/)", parse_mode='MarkdownV2')        
    bot.send_photo(chat_id = message.chat.id, photo = "https://strategiesforinfluence.com/wp-content/uploads/2019/12/Ansoff-Matrix.jpg")
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 

# MARKETING TOOLS    
@bot.message_handler(func = lambda message: message.text == 'Marketing tools')
def send_text(message):
    keyboard = telebot.types.ReplyKeyboardMarkup() 
    bot.send_message(message.chat.id, 'You have chosen marketing studies. Wonderful!', reply_markup = keyboard, parse_mode = 'markdown')
    keyboard.row('Marketing Mix')   
    keyboard.row("Competitors Analysis")
    keyboard.row('Customer Segmentation')
    keyboard.row('CJM')
    keyboard.row('Start')
    bot.send_message(message.chat.id, '*Choose one among them:*', reply_markup = keyboard, parse_mode = 'markdown')   
@bot.message_handler(func = lambda message: message.text == 'Marketing Mix')
def send_text(message):
    bot.send_message(message.chat.id, "The marketing mix refers to the set of actions, or tactics, that a company uses to promote its brand or product in the market. The 4Ps make up a typical marketing mix - Price, Product, Promotion and Place. However, nowadays, the marketing mix increasingly includes several other Ps like Packaging, Positioning, People and even Politics as vital mix elements. Price: refers to the value that is put for a product. It depends on costs of production, segment targeted, ability of the market to pay, supply - demand and a host of other direct and indirect factors. There can be several types of pricing strategies, each tied in with an overall business plan. Pricing can also be used a demarcation, to differentiate and enhance the image of a product. Product: refers to the item actually being sold. The product must deliver a minimum level of performance; otherwise even the best work on the other elements of the marketing mix won't do any good. Place: refers to the point of sale. In every industry, catching the eye of the consumer and making it easy for her to buy it is the main aim of a good distribution or 'place' strategy. Retailers pay a premium for the right location. In fact, the mantra of a successful retail business is 'location, location, location'. Promotion: this refers to all the activities undertaken to make the product or service known to the user and trade. This can include advertising, word of mouth, press reports, incentives, commissions and awards to the trade. It can also include consumer schemes, direct marketing, contests and prizes.")
    bot.send_photo(chat_id = message.chat.id, photo = "https://cdn.business2community.com/wp-content/uploads/2020/03/marketingmixdiagram.jpg")
    bot.send_message(message.chat.id, "[Additional information:](https://www.professionalacademy.com/blogs-and-advice/marketing-theories---the-marketing-mix---from-4-p-s-to-7-p-s)", parse_mode='MarkdownV2')            
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 
@bot.message_handler(func = lambda message: message.text == "Competitors Analysis")
def send_text(message):
    bot.send_message(message.chat.id, "A competitive analysis is a critical part of your company marketing plan. With this evaluation, you can establish what makes your product or service unique--and therefore what attributes you play up in order to attract your target market. Evaluate your competitors by placing them in strategic groups according to how directly they compete for a share of the customer's dollar. For each competitor or strategic group, list their product or service, its profitability, growth pattern, marketing objectives and assumptions, current and past strategies, organizational and cost structure, strengths and weaknesses, and size (in sales) of the competitor's business. A quick and easy way to compare your product or service with similar ones on the market is to make a competition grid. Down the left side of a piece of paper, write the names of four or five products or services that compete with yours. To help you generate this list, think of what your customers would buy if they didn't buy your product or service. Across the top of the paper, list the main features and characteristics of each product or service. Include such things as target market, price, size, method of distribution, and extent of customer service for a product. For a service, list prospective buyers, where the service is available, price, website, toll-free phone number, and other features that are relevant. A glance at the competition grid will help you see where your product fits in the overall market.")
    bot.send_photo(chat_id = message.chat.id, photo = "https://172yv5uzmfx1i8apy2vvn3vs-wpengine.netdna-ssl.com/wp-content/uploads/2019/06/competitor-analysis.png")
    bot.send_message(message.chat.id, "[Additional information:](https://buffer.com/library/competitor-analysis/)", parse_mode='MarkdownV2')                
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 
@bot.message_handler(func = lambda message: message.text == "Customer Segmentation")
def send_text(message):
    bot.send_message(message.chat.id, "Customer segmentation is the practice of dividing a company’s customers into groups that reflect similarity among customers in each group. The goal of segmenting customers is to decide how to relate to customers in each segment in order to maximize the value of each customer to the business. Customer segmentation has the potential to allow marketers to address each customer in the most effective way. Using the large amount of data available on customers (and potential customers), a customer segmentation analysis allows marketers to identify discrete groups of customers with a high degree of accuracy based on demographic, behavioral and other indicators. Since the marketer’s goal is usually to maximize the value (revenue and/or profit) from each customer, it is critical to know in advance how any particular marketing action will influence the customer. Ideally, such “action-centric” customer segmentation will not focus on the short-term value of a marketing action, but rather the long-term customer lifetime value (CLV) impact that such a marketing action will have. Thus, it is necessary to group, or segment, customers according to their CLV.")
    bot.send_photo(chat_id = message.chat.id, photo = "https://www.ebcg.com/wp-content/uploads/2017/09/Market-Segmentation-1-600x442.jpg")
    bot.send_message(message.chat.id, "[Additional information:](https://looker.com/blog/creating-actionable-customer-segmentation-models)", parse_mode='MarkdownV2')                    
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 
@bot.message_handler(func = lambda message: message.text == 'CJM')
def send_text(message):
    bot.send_message(message.chat.id, "A customer journey map is a diagram (or several diagrams) that depict the stages customers go through when interacting with a company, from buying products online to accessing customer service on the phone to airing grievances on social media. To create effective visual maps that reflect customers' journeys through these channels, journey maps must be rooted in data-driven research and must visually represent the different phases customers experience based on a variety of dimensions, including customer sentiment, goals and touch points.")
    bot.send_photo(chat_id = message.chat.id, photo = "https://static.probusiness.by/n/00/d/customer-journey.jpg")
    bot.send_message(message.chat.id, "[Additional information:](https://www.visual-paradigm.com/guide/customer-experience/what-is-customer-journey-mapping/)", parse_mode='MarkdownV2')                    
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 

# FINANCIAL TOOLS    
@bot.message_handler(func = lambda message: message.text == 'Financial tools')
def send_text(message):
    keyboard = telebot.types.ReplyKeyboardMarkup() 
    bot.send_message(message.chat.id, "You have chosen financial studies. Ain't you the next Yoren Buffet?", reply_markup = keyboard, parse_mode = 'markdown')
    keyboard.row('NPV')   
    keyboard.row('Payback Period')
    keyboard.row('Profitability Index')
    keyboard.row('IRR')
    keyboard.row('Start')
    bot.send_message(message.chat.id, '*Choose one among them:*', reply_markup = keyboard, parse_mode = 'markdown')
    
@bot.message_handler(func = lambda message: message.text == 'NPV')
def send_text(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.chat.id, "Net present value (NPV) is the difference between the present value of cash inflows and the present value of cash outflows over a period of time. NPV is used in capital budgeting and investment planning to analyze the profitability of a projected investment or project.", reply_markup = keyboard, parse_mode = 'markdown')
    bot.send_photo(chat_id = message.chat.id, photo = "https://www.antonpiskun.pro/wp-content/uploads/2020/01/net-present-value-formula.jpg")
    bot.send_message(message.chat.id, "[Additional information:](https://courses.lumenlearning.com/boundless-finance/chapter/net-present-value/)", parse_mode='MarkdownV2')                    
    keyboard.row('YES, of course!')   
    keyboard.row('Start')
    bot.send_message(message.chat.id, 'Hey, young investigator! Do you want to try it now?', reply_markup = keyboard, parse_mode = 'markdown')
    
            
@bot.message_handler(func = lambda message: message.text == 'Payback Period')
def send_text(message):
    bot.send_message(message.chat.id, "The payback period refers to the amount of time it takes to recover the cost of an investment. Simply put, the payback period is the length of time an investment reaches a break-even point. The desirability of an investment is directly related to its payback period. Shorter paybacks mean more attractive investments. Although calculating the payback period is useful in financial and capital budgeting, this metric has applications in other industries. It can be used by homeowners and businesses to calculate the return on energy-efficient technologies such as solar panels and insulation, including maintenance and upgrades.")
    bot.send_photo(chat_id = message.chat.id, photo = "https://www.wallstreetmojo.com/wp-content/uploads/2018/04/Discounted-Payback-Period-Formula.jpg")
    bot.send_message(message.chat.id, "[Additional information:](https://corporatefinanceinstitute.com/resources/knowledge/modeling/payback-period/)", parse_mode='MarkdownV2')                    
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 
@bot.message_handler(func = lambda message: message.text == 'Profitability Index')
def send_text(message):
    bot.send_message(message.chat.id, "The profitability index (PI), alternatively referred to as value investment ratio (VIR) or profit investment ratio (PIR), describes an index that represents the relationship between the costs and benefits of a proposed project. It is calculated as the ratio between the present value of future expected cash flows and the initial amount invested in the project. A higher PI means that a project will be considered more attractive.")
    bot.send_photo(chat_id = message.chat.id, photo = "https://www.wallstreetmojo.com/wp-content/uploads/2019/01/Profitability-Index-Formula.jpg")
    bot.send_message(message.chat.id, "[Additional information:](https://www.thebalancesmb.com/the-profitability-index-392917)", parse_mode='MarkdownV2')                    
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True) 
@bot.message_handler(func = lambda message: message.text == 'IRR')
def send_text(message):
    bot.send_message(message.chat.id, "The internal rate of return is a metric used in financial analysis to estimate the profitability of potential investments. The internal rate of return is a discount rate that makes the net present value (NPV) of all cash flows equal to zero in a discounted cash flow analysis. IRR calculations rely on the same formula as NPV does.")
    bot.send_photo(chat_id = message.chat.id, photo = "https://assets1.cleartax-cdn.com/s/img/2019/07/03131911/Internal-Rate-of-Return.png")
    bot.send_message(message.chat.id, "[Additional information:](https://www.accaglobal.com/in/en/student/exam-support-resources/foundation-level-study-resources/ffm/ffm-technical-articles/the-internal-rate-of-return.html)", parse_mode='MarkdownV2')                    
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True)

@bot.message_handler(func = lambda message: message.text == 'YES, of course!')
def mychat(message):
    markup = telebot.types.ReplyKeyboardRemove(selective = False)
    msg = bot.send_message(message.chat.id, 'Hi, pure genius, enter your CF:', reply_markup = markup)
    bot.register_next_step_handler(msg, process_num1_step)
    
def process_num1_step(message, user_result = None):
    try:
        global user_num1
        if user_result == None: user_num1 = float(message.text)
        else: user_num1 = str(user_result)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
        msg = bot.send_message(message.chat.id, "Now...Enter your discount rate (fraction with a dot):", reply_markup = markup)
        bot.register_next_step_handler(msg, process_num2_step)
    except Exception as e: 
        bot.reply_to(message, 'Something went wrong or you typed not a number! Please type "Start" to return to the main menu!') 
        
def process_num2_step(message, user_result = None):
    try:
        global user_num2
        if user_result == None and float(message.text) <= float(1): user_num2 = float(message.text)
        else: user_num2 = str(user_result)
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
        msg = bot.send_message(message.chat.id, "OK, more than a half of the way is done. Let's input periods! Be sure that the number is an integer!", reply_markup = markup)
        bot.register_next_step_handler(msg, process_num3_step)
    except Exception as e: 
        bot.reply_to(message, 'Something went wrong or you typed not a number! Please type "Start" to return to the main menu!')
        
def process_num3_step(message, user_result = None):
    try:
        global user_num3
        if user_result == None: user_num3 = int(message.text)
        else: user_num3 = str(user_result)
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
        msg = bot.send_message(message.chat.id, "Last, but not least! Investments!!!", reply_markup = markup)
        bot.register_next_step_handler(msg, process_num4_step)
    except Exception as e: 
        bot.reply_to(message, 'Something went wrong or you typed not a number! Please type "Start" to return to the main menu!')
        
def process_num4_step(message, user_result = None):
    try:
        global user_num4
        if user_result == None: user_num4 = float(message.text)
        else: user_num4 = str(user_result)
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
        itembtn1 = types.KeyboardButton('Result')
        itembtn2 = types.KeyboardButton('Start')
        markup.add(itembtn1, itembtn2)
        msg = bot.send_message(message.chat.id, "Do you want to see a result or сomeback to the main menu?", reply_markup = markup)
        bot.register_next_step_handler(msg, process_alternative_step)
    except Exception as e: 
        bot.reply_to(message, 'Something went wrong or you typed not a number! Please type "Start" to return to the main menu!')  

def process_alternative_step(message):
    try:
        calc()
        markup = types.ReplyKeyboardRemove(selective = False)
        if message.text.lower() == 'result': bot.send_message(message.chat.id, calc(), reply_markup = markup)
        elif message.text.lower() == 'start': process_num1_step(message.chat.id, user_result)
    except Exception as e: 
        bot.reply_to(message, 'Please, press one more time on "Start" to return to the main menu!')
    
def calc():
    global user_num1, user_num2, user_num3, user_num4, user_result
    user_result = [user_num1 / (1 + user_num2) ** i for i in range(1, user_num3 + 1)]
    return round(sum(user_result) - user_num4, 2)

bot.enable_save_next_step_handlers(delay = 2)
bot.load_next_step_handlers()

if __name__ == '__main__': bot.polling(none_stop = True)


# In[ ]:




