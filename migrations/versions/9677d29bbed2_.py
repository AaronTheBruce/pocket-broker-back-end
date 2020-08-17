"""empty message

Revision ID: 9677d29bbed2
Revises: 
Create Date: 2020-08-17 12:18:49.723615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9677d29bbed2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cryptos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('symbol', sa.String(length=3), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('hashed_password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('event_configs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_frame', sa.String(), nullable=False),
    sa.Column('percent_change', sa.Float(), nullable=False),
    sa.Column('usd_sell_price', sa.Float(), nullable=True),
    sa.Column('usd_buy_price', sa.Float(), nullable=True),
    sa.Column('usd_buy_power', sa.Float(), nullable=True),
    sa.Column('crypto_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['crypto_id'], ['cryptos.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('watch_list_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('crypto_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['crypto_id'], ['cryptos.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usd_start_price', sa.Float(), nullable=False),
    sa.Column('usd_end_price', sa.Float(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('event_config_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_config_id'], ['event_configs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notifications')
    op.drop_table('events')
    op.drop_table('watch_list_items')
    op.drop_table('event_configs')
    op.drop_table('users')
    op.drop_table('cryptos')
    # ### end Alembic commands ###