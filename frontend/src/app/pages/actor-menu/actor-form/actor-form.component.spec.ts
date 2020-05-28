import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { actorFormComponent } from './actor-form.component';

describe('actorFormComponent', () => {
  let component: actorFormComponent;
  let fixture: ComponentFixture<actorFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ actorFormComponent ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(actorFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
