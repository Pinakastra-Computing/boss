"""Move customer's detailed info into separate tables

Revision ID: 14ed44ca815
Revises: 58bbe565915
Create Date: 2015-07-21 16:20:29.986031

"""

# revision identifiers, used by Alembic.
revision = '14ed44ca815'
down_revision = '1d3806228da'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entity_customer_info',
    sa.Column('info_id', sa.Integer(), nullable=False),
    sa.Column('contract_number', sa.String(length=64), nullable=True),
    sa.Column('contract_date', sa.Date(), nullable=True),
    sa.Column('organization_type', sa.String(length=8), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('full_organization_name', sa.String(length=254), nullable=True),
    sa.Column('primary_state_registration_number', sa.String(length=16), nullable=True),
    sa.Column('individual_tax_number', sa.String(length=16), nullable=True),
    sa.Column('legal_address_country', sa.String(length=32), nullable=True),
    sa.Column('legal_address_city', sa.String(length=32), nullable=True),
    sa.Column('legal_address_address', sa.String(length=254), nullable=True),
    sa.Column('location_country', sa.String(length=32), nullable=True),
    sa.Column('location_city', sa.String(length=32), nullable=True),
    sa.Column('location_address', sa.String(length=254), nullable=True),
    sa.Column('general_manager_name', sa.String(length=254), nullable=True),
    sa.Column('general_accountant_name', sa.String(length=254), nullable=True),
    sa.Column('contact_person_name', sa.String(length=254), nullable=True),
    sa.Column('contact_person_position', sa.String(length=64), nullable=True),
    sa.Column('contact_telephone', sa.String(length=16), nullable=True),
    sa.Column('contact_email', sa.String(length=254), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('info_id')
    )
    op.create_index(op.f('ix_entity_customer_info_customer_id'), 'entity_customer_info', ['customer_id'], unique=False)
    op.create_table('private_customer_info',
    sa.Column('info_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('country', sa.String(length=32), nullable=True),
    sa.Column('city', sa.String(length=32), nullable=True),
    sa.Column('address', sa.String(length=254), nullable=True),
    sa.Column('passport_series_number', sa.String(length=16), nullable=True),
    sa.Column('passport_issued_by', sa.String(length=254), nullable=True),
    sa.Column('passport_issued_date', sa.Date(), nullable=True),
    sa.Column('telephone', sa.String(length=16), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('info_id')
    )
    op.create_index(op.f('ix_private_customer_info_customer_id'), 'private_customer_info', ['customer_id'], unique=False)

    op.execute("INSERT INTO private_customer_info (customer_id, birthday, address, name, city, telephone, country) "
               "SELECT customer.customer_id, customer.birthday, customer.address, customer.name, customer.city, "
               "customer.telephone, customer.country FROM customer "
               "WHERE customer_type='private' AND (customer.birthday IS NOT NULL OR customer.address IS NOT NULL OR "
               "customer.name IS NOT NULL OR customer.city IS NOT NULL OR customer.telephone IS NOT NULL OR "
               "customer.country IS NOT NULL)")

    op.execute("INSERT INTO entity_customer_info (customer_id, legal_address_address, name, legal_address_city, "
               "contact_telephone, legal_address_country) "
               "SELECT customer.customer_id, customer.address, customer.name, customer.city, customer.telephone, "
               "customer.country FROM customer "
               "WHERE customer_type='entity' AND (customer.address IS NOT NULL OR customer.name IS NOT NULL OR "
               "customer.city IS NOT NULL OR customer.telephone IS NOT NULL OR customer.country IS NOT NULL)")

    op.drop_column('customer', 'country')
    op.drop_column('customer', 'telephone')
    op.drop_column('customer', 'name')
    op.drop_column('customer', 'address')
    op.drop_column('customer', 'birthday')
    op.drop_column('customer', 'city')
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('city', mysql.VARCHAR(length=32), nullable=True))
    op.add_column('customer', sa.Column('birthday', sa.DATE(), nullable=True))
    op.add_column('customer', sa.Column('address', mysql.VARCHAR(length=254), nullable=True))
    op.add_column('customer', sa.Column('name', mysql.VARCHAR(length=64), nullable=True))
    op.add_column('customer', sa.Column('telephone', mysql.VARCHAR(length=16), nullable=True))
    op.add_column('customer', sa.Column('country', mysql.VARCHAR(length=32), nullable=True))

    op.execute("UPDATE customer, private_customer_info "
               "SET customer.birthday=private_customer_info.birthday, customer.address=private_customer_info.address, "
               "customer.name=private_customer_info.name, customer.city=private_customer_info.city, "
               "customer.telephone=private_customer_info.telephone, customer.country=private_customer_info.country "
               "WHERE private_customer_info.customer_id = customer.customer_id")

    op.execute("UPDATE customer, entity_customer_info "
               "SET customer.address=entity_customer_info.legal_address_address, "
               "customer.name=entity_customer_info.name, customer.city=entity_customer_info.legal_address_city, "
               "customer.telephone=entity_customer_info.contact_telephone, "
               "customer.country=entity_customer_info.legal_address_country "
               "WHERE entity_customer_info.customer_id = customer.customer_id")

    op.drop_constraint(op.f('private_customer_info_ibfk_1'), 'private_customer_info', type_='foreignkey')
    op.drop_index(op.f('ix_private_customer_info_customer_id'), table_name='private_customer_info')
    op.drop_table('private_customer_info')
    op.drop_constraint(op.f('entity_customer_info_ibfk_1'), 'entity_customer_info', type_='foreignkey')
    op.drop_index(op.f('ix_entity_customer_info_customer_id'), table_name='entity_customer_info')
    op.drop_table('entity_customer_info')
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass
